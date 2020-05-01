from testapp.models import Data2, Datax
import sys
from tqdm import tqdm
import datetime


class QuerySets:

    def __init__(self):
        self.new_coding = []
        self.new_result = dict()
        self.tag_result = dict()
        return

    # @staticmethod
    def handle_elements_list(self, ele1, ele2):
        coding = Data2.objects.all()
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
                self.new_coding.append(new_data)
        # print('new_coding={}'.format(self.new_coding))
        # return self.new_coding

    def handle_dict(self):
        result = dict()
        for data in tqdm(self.new_coding):
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
        for text, el in result.items():
            one_group = result[text]
            if len(one_group) > 1:
                standard = 0
                a += 1
                for label, bscode in one_group.items():
                    if len(bscode) > standard:
                        standard_label = label
                        standard = len(bscode)
                self.new_result[text] = el
        return self.new_result

    def change_original_dict(self):
        if not bool(self.new_result):
            print("税号分组的编码字典为空！")
            return
        data = list()
        label = dict()
        for main_lable, text in tqdm(self.new_result.items()):
            label[main_lable] = []
            # print('我想看看text{}'.format(text))
            for shuihao, bsnumber in text.items():
                # bsnumber = tuple(tuple(w) for w in bsnumber)
                # print('bsnumber是多少{}'.format(bsnumber))
                for bs in bsnumber:
                    a = Datax.objects.get(customs_id=bs[0], product_number=bs[1])
                    label[main_lable].append(a)
                    # print(a.product_name)
        # print(label)
        return label

    def tax_result(self, groups):
        new_result = list()
        for key, values in groups.items():
            old_key = key
            tag_list = []
            end = 0  # 标准
            big_end = 0  # 最大
            small_end = 0  # 最小
            standard_tag = 0.0  # 标准税率
            big_tag = 0.0  # 最大税率
            small_tag = 0.0  # 最小税率
            standard_label = key  # 标准税号
            big_label = key  # 最大税号
            small_label = key  # 最小税号
            product_tags_nums = dict()
            # print('values======{}'.format(values))
            for t in values:
                try:
                    label = t.product_id
                    tag = float(t.shi_jia_guan)
                    if label in product_tags_nums.keys():
                        product_tags_nums[label][0] += 1
                    else:
                        product_tags_nums[label] = [1] + [tag]
                except:
                    print(t)
                    sys.exit()
            # print('yessssssssssssssss{}'.format(product_tags_nums))

            s_number = 0  # 标准
            sb_number = 0  # 最大
            ss_number = 0  # 最小
            s_gs = 0.0  # 标准
            sb_gs = 0.0  # 最大
            ss_gs = 0.0  # 最小
            for i, (k, value) in enumerate(product_tags_nums.items()):
                if i == 0:  # 首先把首位变成标准值
                    s_number = sb_number = ss_number = value[0]
                    s_gs = sb_gs = ss_gs = value[1]
                    standard_label = k
                    small_label = k
                    big_label = k
                else:
                    if value[0] > s_number:
                        s_number = value[0]
                        s_gs = value[1]
                        standard_label = k
                    if value[0] == s_number:
                        if value[1] < s_gs:
                            s_gs = value[1]
                            standard_label = k
                    if value[1] < ss_gs:  # 最小
                        ss_gs = value[1]
                        small_label = k
                    if value[1] > sb_gs:  # 最大
                        sb_gs = value[1]
                        big_label = k

            for t in values:
                if t.shi_jia_guan != s_gs:
                    tag_list.append(1)
                else:
                    tag_list.append(0)

            self.tag_result[old_key] = tag_list
        return self.tag_result
        # 下面是计算税差的部分
        #     standard_tag = s_gs
        #     big_tag = sb_gs
        #     small_tag = ss_gs
        #     for t in values:
        #         label = t.product_id
        #         tag = float(t.shi_jia_guan)
        #         wsjg = float(t.shui_jia)
        #         if label == standard_label:  # 标准
        #             standard_tag = float(t.shi_jia_guan)
        #             sc = 0
        #         else:
        #             sc = wsjg * (tag - standard_tag)
        #
        #         if label == big_label:  # 最大
        #             big_tag = float(t.shi_jia_guan)
        #             bsc = 0
        #         else:
        #             bsc = wsjg * (tag - big_tag)
        #
        #         if label == small_label:  # 最小
        #             small_tag = float(t.shi_jia_guan)
        #             ssc = 0
        #         else:
        #             ssc = wsjg * (tag - small_tag)
        #
        #         end += sc
        #         big_end += bsc
        #         small_end += ssc
        #
        #     self.tag_result[old_key] = [end, big_end, small_end]
        # print('1111111111111111{}'.format(self.tag_result))
