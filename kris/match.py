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
        
        
        
