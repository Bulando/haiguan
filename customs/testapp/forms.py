from django import forms


class FileUploadForm(forms.Form):
    #name = forms.CharField(max_length=20, min_length=3, required=True, label='名称:')
    #my_file = forms.FileField(label='文件名称:', style="font-size: 30px;")
    #选择文件样式：style="font-size:17px; color:red; margin-left:2%"
    my_file = forms.FileField(label='文件名称:')
