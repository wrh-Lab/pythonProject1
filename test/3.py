"""
编写程序，练习元祖的使用：这份菜单能修改吗？实现如下功能：
将输入的菜单列表menu_list转换成元组类型；
打印输出生成的元组；
打印输出的元组中首字母最大的元素
"""
menu_list = []#定义一个空列表，用来存放从键盘中输入的数据
i = 0 #定义变量赋值为0
#使用while循环，并限制循环次数为3次
while i <= 2:
        food = input("请输入食物名称：")#在键盘上输入食物名称，并将其赋值给变量food，方便下面的操作
        menu_list.append(food)  #将从键盘上输入的食物名称在food中进行暂时的储存，然后依次从列表尾部进行添加
        i += 1 #循环依次次数加一，用来计数方便while循环进行判断，防止进入死循环
menu_tuple = tuple(menu_list) #将列表变成元组形式
print("菜单列表为：",menu_tuple)#输出元组菜单
max_element = max(menu_tuple)#寻找出元组中最大字母的元素
print("菜单列表中首字母最大的元素为：",max_element)
