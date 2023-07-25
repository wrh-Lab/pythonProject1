guests=[]
n=int(input("请输入客人数量:"))#从键盘输入数字，然后转化成整型
for i in range(n):
    guest=input("请输入客人姓名：")
    guests.append(guest)
print("最初客人名单为：{}".format(guests))
print("删除名单中排在最后的客人：")
deleted_guest=guests.pop(len(guests)-1)
print("被删除客人的名字为：{}".format(deleted_guest))
print("删除最后一个客人的名单为：{}".format(guests))
print("将被删除的客人插入索引为2的位置：")
guests.insert(2,deleted_guest)
print('被删除索引为1的客人为:')
del(guests[1])
print("删除以后的名单为:{}".format(guests))