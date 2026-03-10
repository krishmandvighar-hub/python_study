print("hello")
name =input("enter the student name: ")
print(name)
physics=int(input("enter the phy marks "))
chemistry=int(input("enter the chem marks "))
english=int(input("enter the eng marks "))
maths=int(input("enter the math marks "))
it=int(input("enter the it marks "))
economics=int(input("enter the eco marks" ))
total=(physics+chemistry+english+maths+it+economics)
per=total/6
print("total marks",total)
print("percentage marks",per)

if per>100:
    print("invalid output")
elif per>90:
    print("+A")
elif per>80:
    print("A")
elif per>70:    
    print("+B")
elif per>60:    
    print("B")
elif per>50:    
    print("C")
elif per>35:    
    print("D")
else:
    print("fail")

