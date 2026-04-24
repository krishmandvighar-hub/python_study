print("a > b")
a = int(input("enter the num : "))
b = int(input("enter the num : "))
print("true") if a > b else print("false")


print("who is bigger c or d")
c = int(input("enter the num : "))
d = int(input("enter the num : "))
bigger = c if c > d else d
print("Bigger is: ", bigger)

e = int(input("enter the num : "))
f = int(input("enter the num : "))
print("A") if e > f else print("=") if e == f else print("B")

x = int(input("enter the num : "))
y = int(input("enter the num : "))
max_value = x if x > y else y
print("Maximum value:", max_value)

username = input("enter the username : ")
display_name = username if username else "Guest"
print("Welcome,", display_name)


