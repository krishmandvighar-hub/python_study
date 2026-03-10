x = int(input("enter the any number: "))
y = int(input("enter the any number: "))
sign=input("choose any the sign(+,-,*,/) : ")
match sign:
    case "+" :
        print(x+y)
    case "-" :
        print(x-y)
    case "*" :
        print(x*y)
    case "/" :
        print(x/y)
    case _:
        print("not valid")
