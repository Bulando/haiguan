from testapp.models import Data2
import sys
from tqdm import tqdm
import datetime


class QuerySets:

    def __init__(self):
        self.new_coding = []
        self.new_result = dict()
        return

    # @staticmethod
    def handle_elements_list(self, ele1, ele2):
        coding = Data2.objects.all()
        print('coding = {}'.format(len(coding)))
        # new_coding = list()
        for date in tqdm(coding):
            if ele1 in date[3] and ele2 in date[3]:
                el = date[3][date[3].index(ele1):]
                el1 = el[:el.find(',')]
                ell = date[3][date[3].index(ele2):]
                el2 = ell[:el.find(',')]
                el = el1 + ',' + el2
                new_data = list(date[:3]) + el
                self.new_coding.append(new_data)
        print('new_coding={}'.format(len(self.new_coding)))
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


    