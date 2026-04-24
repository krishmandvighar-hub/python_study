#day

day = int(input("Enter any day number: "))
match day:
    case 1:
       print("Mon")
    case 2:
        print("Tues")
    case 3:
       print("Wed")
    case 4:
        print("Thur")
    case 5:
       print("Fri")
    case 6:
        print("Sat")
    case 7:
        print("Sun")
    case _:
        print("Invalid day ")

alpha = input("Enter any alphabet: ")
match alpha:
    case 'a'|'e'|'i'|'o'|'u'|'A'|'E'|'I'|'O'|'U':
        print(alpha , 'is a vowel')
    case _:
        print(alpha, 'is a consonant')
        
#month
        
month = input("enter any month: ")
match month:
    case "January"|"March"|"May"|"July"|"August"|"October"|"December" :
        print(month, "has 31 days")
    case "April"|"June"|"September"|"November" :
        print(month, "has 30 days")
    case "February":    
        print(month, "has 28 days")
    case _:
        print("invalid")
        
#calculator
        
x = int(input("enter the any number: "))
y = int(input("enter the any number: "))
sign = input("choose any the sign(+,-,*,/) : ")
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

