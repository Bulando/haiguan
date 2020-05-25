from testapp.models import Datax, Data2
import sys
from tqdm import tqdm
import numpy as np

HighestLevel = 'f'
IVLevel = 'e'
IIIlevel = 'd'
IILevel = 'c'
ILevel = 'b'
LowestLevel = 'a'
BigLevel = ''
SmallLevel = ''


class coreTax:

    def __init__(self):
        self.res = dict()
        return

    @staticmethod
    def handle_elements_list(ele1, ele2, filter_ele_list):
        coding = Data2.objects.all()[:10000]
        print('coding = {}'.format(len(coding)))
        # new_coding = list()
        for date in coding:
            # print('我来问你来猜 {}'.format(date.customs_id))
            if ele1 in date.elements and ele2 in date.elements:
                el = date.elements[date.elements.index(ele1):]
                el1 = el[:el.find(',')]
                ell = date.elements[date.elements.index(ele2):]
                el2 = ell[:el.find(',')]
                el = el1 + ',' + el2
                val = date.customs_id, date.product_number, date.product_id
                new_data = list(val) + [el]
                filter_ele_list.append(new_data)

    @staticmethod
    def handle_dict(filter_ele_list):
        result = dict()
        for data in tqdm(filter_ele_list):
            big = data[0]
            small = data[1]
            label = data[2]
            text = data[3]
            if text not in result.keys():
                result[text] = dict()
            if label not in result[text].keys():
                result[text][label] = []
            result[text][label].append([big] + [small])
        a = 0
        # new_result = dict()
        differ_label_res = dict()
        same_label_res = dict()
        for text, el in result.items():
            one_group = result[text]
            # if len(one_group) > 1:
            differ_label_res[text] = el
            # else:
            #     same_label_res[text] = el
        return differ_label_res

    def change_original_dict(self, label_res_tuple):
        if not bool(label_res_tuple):
            print("税号分组的编码字典为空！")
            return
        data = list()
        for main_lable, text in tqdm(label_res_tuple.items()):
            self.res[main_lable] = []
            # print('我想看看text{}'.format(text))
            for shuihao, bsnumber in text.items():
                for bs in bsnumber:
                    # 海关编号和商品序号理论上只应有1个，去重工作要确保这一点
                    a = Datax.objects.get(customs_id=bs[0], product_number=bs[1])
                    self.res[main_lable].append(a)
                    # print(a.product_name)
        # print(label)
        # return self.res

    def product_tax_num(self, values):
        product_tags_nums = {}
        for t in values:
            try:
                label = t.product_id
                tag = t.shi_jia_guan
                if label not in product_tags_nums.keys():
                    product_tags_nums[label] = dict()
                if tag not in product_tags_nums[label].keys():
                    product_tags_nums[label][tag] = 1
                else:
                    product_tags_nums[label][tag] += 1
            except:
                print(t)
                sys.exit()
        return product_tags_nums

    def tax_level(self, num, numbers, w, tag):
        if tag == 0:
            tag = "税率最高"
        elif tag == 1:
            tag = "税率最低"
        elif tag == 2:
            tag = "税率偏高"
        elif tag == 3:
            tag = "税率偏低"
        per = (num - w) / numbers
        if per > 0.2:
            per = [HighestLevel] + [tag]
        elif per > 0.16:
            per = [IVLevel] + [tag]
        elif per > 0.12:
            per = [IIIlevel] + [tag]
        elif per > 0.08:
            per = [IILevel] + [tag]
        elif per > 0.04:
            per = [ILevel] + [tag]
        else:
            per = [LowestLevel] + [tag]
        return per

    def core_tax(self, product_tags_nums):
        for label, tags in product_tags_nums.items():
            if len(tags) >= 3:
                numMax = max(tags.values())
                numMin = min(tags.values())
                max_tag = max(tags.keys())
                min_tag = min(tags.keys())
                numMaxLi = []
                label_tagsNums = 0
                for t in tags.keys():
                    if tags[t] == numMax:
                        numMaxLi.append(float(t))
                        label_tagsNums += numMax
                        product_tags_nums[label][t] = [HighestLevel]
                    else:
                        label_tagsNums += numMax
                for tt, v in tags.items():
                    if v != [HighestLevel]:
                        #   如果是最大的税率或最小的税率，加权重
                        if tt == max_tag or tt == min_tag:
                            w = label_tagsNums / 10
                            tag = 0 if (tt == max_tag) else 1
                            product_tags_nums[label][tt] = self.tax_level(product_tags_nums[label][tt], label_tagsNums,
                                                                          w, tag)
                        else:
                            tag = 2 if (float(tt) > np.mean(numMaxLi)) else 3
                            product_tags_nums[label][tt] = self.tax_level(product_tags_nums[label][tt], label_tagsNums,
                                                                          0, tag)
            elif len(tags) == 2:
                numMax = max(tags.values())
                label_tagsNums = 0
                num_tag = list(tags.keys())[list(tags.values()).index(numMax)]
                for t in tags.keys():
                    if t == numMax:
                        label_tagsNums += product_tags_nums[label][t]
                        product_tags_nums[label][t] = [HighestLevel]
                    else:
                        w = 0
                        label_tagsNums += product_tags_nums[label][t]
                        tag = 2 if (t > num_tag) else 3
                        product_tags_nums[label][t] = self.tax_level(product_tags_nums[label][t], label_tagsNums, w,
                                                                     tag)
            else:
                for t in tags.keys():
                    product_tags_nums[label][t] = [HighestLevel]
        return product_tags_nums


    def tax_algorithm(self):
        filter_ele_list = []
        self.handle_elements_list('0000', '0001', filter_ele_list)
        differ_label_res = dict()
        differ_label_res = self.handle_dict(filter_ele_list)
        self.change_original_dict(differ_label_res)
        alas = []
        if not bool(self.res):
            print("税号分组的编码字典为空！")
            return
        # print("-----------{}".format(self.res))
        for key, values in self.res.items():
            product_tags_nums = dict()
            product_tags_nums = self.product_tax_num(values)
            product_tags_nums = self.core_tax(product_tags_nums)
            for v in values:
                la = v.product_id
                ta = v.shi_jia_guan
                if product_tags_nums[la][ta][0] == HighestLevel:
                    continue
                v.tag = product_tags_nums[la][ta][0]
                v.tag_ins = product_tags_nums[la][ta][1]
                alas.append(v)

        return alas
