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
    template_name = 'testapp/test.html'


def detail(request, year):
    try:
        question = Datax.objects.get(pk=year)
    except question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'testapp/detail.html', {'question': question})


def upload(request):
    '''
    :param request:
    :return: 上传文件excel表格 ,并进行解析
    '''
    if request.method == "POST":
        print("post request")
        myform = FileUploadForm(request.POST, request.FILES)

        # 在这里可以添加筛选excel的机制
        if myform.is_valid():
            # print(myform)
            f = request.FILES['my_file']
            print(f)

            # 开始解析上传的excel表格
            wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 关键点在于这里
            table = wb.sheets()[0]
            print("tableee{}".format(table))
            nrows = table.nrows  # 行数
            ncole = table.ncols  # 列数
            print("row :%s, cole: %s" % (nrows, ncole))
            er = ExcelRead(table)
            erli = []
            er.list_data(erli)
            er.handle_uploaded_file(erli)
            print("导入data0表成功！！！")
            # for i in range(1, nrows):
            #     rowValues = table.row_values(i)  # 一行的数据
            #
            #     print(type(rowValues[10]))
            #     R_projectname = rowValues[1]
            #
            #     print('rowValues-->{}'.format(R_projectname))
            #
            #     pf = PhoneMsg.objects.filter(M_name=R_projectname)
            #     # pf = PhoneMsg.objects.all()
            #     if not pf.exists():  # 空值
            #         return render(request, 'rc_test/upFileFail.html',
            #                       context={'error': u'R_projectname 不存在,联系管理员进行添加!'})
            #
            #     print(pf)
            #
            #     pm = PhoneMsg.objects.get(M_name=R_projectname)
            #     pm.save()
            #     re = Result()  # 实例化result表
            #     re.R_projectname = R_projectname
            #     re.R_name = rowValues[2]
            #     re.R_version = rowValues[3]
            #     re.R_context = rowValues[4]
            #     re.R_result = rowValues[5]
            #     re.R_note = rowValues[6]
            #     re.R_ower = rowValues[7]
            #     re.R_kexuan = rowValues[8]
            #     re.R_inning = rowValues[9]
            #     re.R_createtime = datetime(*xldate_as_tuple(rowValues[10], 0))
            #     print(datetime(*xldate_as_tuple(rowValues[10], 0)))
            #     re.save()
            #     pm.result.add(re)
            #
            # handle_upload_file(f, str(f))  # 上传文件处理

        return render(request, "testapp/fileup.html")


    else:
        myform = FileUploadForm()
    return render(request, 'testapp/fileup.html', context={'form': myform, 'what': "文件传输"})
