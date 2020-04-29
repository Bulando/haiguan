from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from testapp.querysets import QuerySets


def index(request):
    result = dict()
    qs = QuerySets()
    qs.handle_elements_list('0000', '0001')
    result = qs.handle_dict()
    x = dict()
    x = qs.change_original_dict()
    qs.tax_result(x)
    return HttpResponse('hello world david')
