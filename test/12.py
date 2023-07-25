"""
已知列表data中有若干字符串，要求编写程序，对data中的字符串进行过滤，只输出重复字符不超过一半的字符串
"""
data=['sf','fsssfs','dsgdfg','ertwe','dfdddddd']
def f(s):
    for c in s:
        if s.count(c) > len(s)/2:
            return False
        return True
y=list(filter(lambda x:f(x),data))
print(y)