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
