def divide(x,y):
 try:
    result=x/y
 except ZeroDivisionError:
    print("division by zero!")
 else:
    print("result is",result)
 finally:
    print("executing finally clause")
d=divide(1,2)
print("\n")
d=divide(2,0)
print("\n")
d=divide("2","1")
