"""
编写一个程序，实现列元素的排序：输入客人名单，然后按照名字排序。
"""
source_list=[]#定义一个列表用来存放输入的姓名元素
#使用while循环，将客人名字依次从键盘上输入到列表中
while True:
    list_element=input("请输入客人姓名：")  #在键盘上输入客人的姓名，一般输入的字符型
    source_list.append(list_element)  #将在键盘上输入的客人姓名依次添加到列表尾部
    a=input("是否结束？yes or no:") #定义一个变量，从键盘上输入yes or no 用来判断是否结束运行
    if a.lower() in {"yes"}:  #将在键盘上输入的单词转化成小写再与yes进行对照判断是否相等，如果相等将结束循环，如果不相等将继续循环
        break
"""
格式化字段（括号及其里面的字符）将会被format()中的参数替换,在format()中使用关键字参数，
它们的值会指向使用该名字的参数，同时位置和关键字参数可相互结合
"""
print("排序前的客人名单为：{}".format(source_list))
source_list.sort(key=lambda x:len(str(x)))#按转换后的字符串的长度进行排序
print("排序后的客人名单为：{}".format(source_list))