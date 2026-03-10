print("Calculator")
num1 =int(input("enter the number: "))
num2 =int(input("enter the number: "))
sign=input("choose any the sign(+,-,*,/) : ")
if sign=='+':
    print(num1+num2)
elif sign=='-':
    print(num1-num2)
elif sign=='*':
    print(num1*num2)
elif sign=='/':
    print(num1/num2)

else:
    print("invalid sign")

