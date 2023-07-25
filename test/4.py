"""
编写程序，练习字典的使用：这份菜单可以修改
"""
menu_dict={}
while True:
    food1 = input("请输入菜品名称：")
    price=int(input("请输入菜品价格："))
    menu_dict[food1]=price
    print(food1, price)
    b=input("是否对其修改？yes or no:")
    if b.lower() in {'yes'}:
        food=input("修改菜名：")
        price=int(input("菜名价格："))
        menu_dict[food] = price
        print(menu_dict)
    a=input("是否结束输入菜名和价格？yes or no:")
    if a.lower() in {"yes"}:
        break
#
# menu_dict['lamb']=50
# menu_dict['fish']=100
# fish_price=menu_dict['fish']
# del menu_dict['lamb']
# print(fish_price)
# print(menu_dict)
