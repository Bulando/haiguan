from django.shortcuts import render

# Create your views here.
from .models import Datax
from django.http import HttpResponse, HttpResponseRedirect
from testapp.querysets import QuerySets
from django.template import loader
from django_tables2 import SingleTableView
from .tables import DataxTable


def index(request):
    result = dict()
    qs = QuerySets()
    qs.handle_elements_list('0000', '0001')
    result = qs.handle_dict()
    x = dict()
    y = dict()
    x = qs.change_original_dict()
    y = qs.tax_result(x)
    # print("xxxxxxxxxxx{}".format(x))
    # print("yyyyyyyyyyy{}".format(y))
    dict_groups = []
    for key, values in x.items():
        tags = y.get(key)
        if len(tags) == 0 or len(tags) != len(values):
            print("数据字典和标记字典不对应！")
            break
        for i in range(len(values)):
            dict_groups.append([values[i]] + [tags[i]])
        # dict_groups.append(values + [tags])
    print("lalalalalalalalala{}".format(dict_groups))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    return render(request, 'testapp/index.html', {'context': dict_groups})


class DataxListView(SingleTableView):
    model = Datax
    table_class = DataxTable
    template_name = 'testapp/test.html'
