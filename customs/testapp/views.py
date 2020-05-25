import csv

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
from .forms import FileUploadForm
import xlrd
from testapp.excelHandler import ExcelRead
from testapp.coreAlgrithm import coreTax

def index(request):
    result = dict()
    qs = QuerySets()
    qs.handle_elements_list('0000', '0001')
    result = qs.handle_dict()
    x = dict()
    y = dict()
    x = qs.change_original_dict()
    y = qs.tax_result(x)
    dict_groups = []
    for key, values in x.items():
        tags = y.get(key)
        if len(tags) == 0 or len(tags) != len(values):
            print("数据字典和标记字典不对应！")
            break
        for i in range(len(values)):
            values[i].name = tags[i]
            jiba = Datax.objects.get(id=values[i].id)
            jiba.name = tags[i]
            # jiba.save()
            dict_groups.append(values[i])
            # dict_groups.append([values[i]] + [tags[i]])
    return render(request, 'testapp/index.html', {'context': dict_groups})


class DataxListView(SingleTableView):
    core = coreTax()
    z = core.tax_algorithm()
    model = Datax
    table_class = DataxTable
    table_data = z
    # table_class.order_by = "product_id"
    template_name = 'testapp/test.html'


def detail(request, year):
    try:
        question = Datax.objects.get(pk=year)
    except question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'testapp/detail.html', {'question': question})


def upload(request):
    """
    :param request:
    :return: 上传文件excel表格 ,并进行解析
    """
    if request.method == "POST":
        print("post request")
        myform = FileUploadForm(request.POST, request.FILES)
        # 在这里可以添加筛选excel的机制
        if myform.is_valid():
            erli = []
            f = request.FILES['my_file']
            path = f.temporary_file_path()
            nessEle = ["海关编号", "商品序号", "商品编号", "商品名称", "规格型号"]
            er = ExcelRead()
            if path.endswith('.xls'):
                wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 关键点在于这里
                table = wb.sheets()[0]
                er.list_data(erli, table, table.nrows)
                er.handle_uploaded_file(erli)
            if path.endswith('.csv'):
                # csv格式读取数据，f为上传的文件
                with open(path, newline='') as rfile:
                    reader = csv.reader(rfile, dialect='excel')
                    # 读取第二行数据（表头为第一行）
                    header_row = next(reader)
                    if set(header_row) >= set(nessEle):
                        return
                    for line in reader:
                        erli.append(line)
                    print("erli==={}".format(erli[0]))
                    # er.handle_uploaded_file(erli)
            print("导入data0表成功！！！")
        return render(request, "testapp/fileup.html")
    else:
        myform = FileUploadForm()
    return render(request, 'testapp/fileup.html', context={'form': myform, 'what': "文件传输"})
