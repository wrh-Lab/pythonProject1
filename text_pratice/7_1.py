#向文本文件中写入内容
s = '文本文件的读取方法\n文本文件的写入方法\n'
with open('E:\sample.text', 'a+') as f:
    f.write(s)
#读取并显示文本文件的前5个字符
# with open('E:\sample.text',encoding="utf-8") as fp:
#     for line in fp:
#       print(line)
"""移动指针，然后读取并显示文本文件中的内容
seek()方法将文件指针定位到文件中指定字节的位置。读取时遇到无法解码的字符会自动抛出异常
"""
s='中国山东烟台 SDIBT'
fp=open(r'E:\sample.text','w')
fp.write(s)
fp.close()
fp=open(r'E:\sample.text','r')
print(fp.read(3))
print(fp.seek(2))
print(fp.read(2))
print(fp.seek(13))
print(fp.read(1))
print(fp.seek(15))
print(fp.read(1))
print(fp.seek(3))
print(fp.read(1))