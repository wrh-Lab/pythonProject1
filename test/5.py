"""
编写程序，实现字典的遍历：菜名和价格的展示
"""
menu_dict={}#构造一个空字典用来存放相应的键值对
while True:#使用while循环，用来依次输入菜名和菜名的价格
    try:
        food=input("请输入菜名：")
        price=int(input("请输入菜名的价格："))
        menu_dict[food]=price
    except:
        break
for key in menu_dict.keys():#使用for循环将字典中的键依次打印出来
    print(key,end="")
print("\n")
for key,value in menu_dict.items():#使用for循环依次将字典中的键值依次挑选出来并进行打印
    print(key,value,end='')