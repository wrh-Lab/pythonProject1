"""
编写一个程序，实现字符串拼接：接收用户输入的两个字符串，将它们组合后输出
"""
name=input("请输入一个人的名字：")#从键盘上输入名字并保存在变量name中
country=input("请输入一个国家的名字：")#从键盘上输入国家的名字并保存在country中
print("世界那么大，{}想去{}看看".format(name,country))#使用format()来将输入的姓名和国家名放入相应的位置上