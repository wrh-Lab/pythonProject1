"""
自定义内置异常类来实现自定义的异常类
"""
class ShortInputExpection(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=legth
        self.alteast=atleast
try:
    s=input("请输入-->")
    if len(s)<3:
        raise ShortInputExpection(len(s),3)
except EOFError:
    print("您输入了一个结束标记EOF")
except ShortInputExpection as x:
    print('ShortInputExpection:输入的长度是%d,长度至少应是%d'%(x.length,x.alteast))
else:
    print("没有异常发生。")