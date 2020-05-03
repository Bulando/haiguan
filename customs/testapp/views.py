from django.shortcuts import render

# Create your views here.
from .models import Datax, Dataxx
from django.http import HttpResponse, HttpResponseRedirect
from testapp.querysets import QuerySets
from django.template import loader
from django_tables2 import SingleTableView
from .tables import DataxTable
from django.views.generic.edit import BaseDetailView, UpdateView
from django.http import Http404

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
            values[i].name = tags[i]
            jiba = Dataxx.objects.get(id=values[i].id)
            jiba.name = tags[i]
            # jiba.save()
            dict_groups.append(values[i])
            # dict_groups.append([values[i]] + [tags[i]])

    print("lalalalalalalalala{}".format(dict_groups))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    return render(request, 'testapp/index.html', {'context': dict_groups})


class DataxListView(SingleTableView):
    result = dict()
    qs = QuerySets()
    qs.handle_elements_list('0000', '0001')
    result = qs.handle_dict()
    x = dict()
    y = dict()
    x = qs.change_original_dict()
    y = qs.tax_result(x)
    print("yaaaaaaaaaaaa{}".format(y))
    dict_groups = []
    for key, values in x.items():
        tags = y.get(key)
        if len(tags) == 0 or len(tags) != len(values):
            print("数据字典和标记字典不对应！")
            break
        for i in range(len(values)):
            values[i].tag = tags[i]
            print("taggg={}".format(values[i].tag))
            dict_groups.append(values[i])
    model = Datax
    table_class = DataxTable
    table_data = dict_groups
    template_name = 'testapp/test.html'


def detail(request, year):
    try:
        question = Datax.objects.get(pk=year)
    except question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'testapp/detail.html', {'question': question})
