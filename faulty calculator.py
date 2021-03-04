
import time
try:
    print("input frist value")
    num1= float(input())
    print("input second value")
    num2= float(input())
    print("input(+,/,*,-)")
    CV = input()
    if CV=='+' and num1==55 and num2==2:
        print("12")
        localtime =time.time()
        print(localtime)
    elif CV=='-' and num1==25 and num2==3:
        print("32")
        localtime =time.time()
        print(localtime)
    elif CV=='/' and num1==44 and num2==8:
        print("22")
        localtime =time.time()
        print(localtime)
    elif CV=='*' and num1==510 and num2==6:
        print("10")
        localtime =time.time()
        print(localtime)
    elif CV=='+':
        print(num1+num2)
        localtime =time.time()
        print(localtime)
    elif CV=='-':
        print(num1-num2)
        localtime =time.time()
        print(localtime)
    elif CV=='*':
        print(num1*num2)
        localtime =time.time()
        print(localtime)
    elif CV=='/':
        print(num1/num2)
        localtime =time.time()
        print(localtime)
    else:
        print("vilaid")
except:
    print("somthing wrong")



    
    
    
