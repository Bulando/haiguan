'''
# csv格式读取数据，f为上传的文件
with open(f, newline='') as rfile:
    reader = csv.reader(rfile, dialect='excel')
    # 读取第二行数据（表头为第一行）
    header_row = next(reader)
# 写入数据到数据库中
with open('aaa', 'w') as wfile:
    write = csv.writer(wfile)
    for row in header_row:
        write.writerow(row)
erli = []
write.list_data(erli)
write.handle_uploaded_file(erli)
print("导入data0表成功！！！")
'''
