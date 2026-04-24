#---------------------------------------------------------------
def x(fun):
    def inn(n):
        return fun(n).upper()
    return inn
    
@x    
def y(n):
    return "hello!"+ n
    
print(y("kris"))

#----------------------------------------------------------------
def a(f):
    def a(fun):
        def inner(num):
            if f==1:
                return fun(num).upper()

            elif f==2:
                return fun(num).lower()
            else:
                return "invalid case number"
        return inner
    return a

def b(fu):
    def inn(num):
        return num +""+ "welcome!"
    return inn

name=input("enter your name : ")
print("upper for 1 or lower of 2:")
number = int(input("enter any num: "))

@a(number)
@b
def zorock(num):
    return num

print(zorock(name))

#--------------------------------------------------------------------
