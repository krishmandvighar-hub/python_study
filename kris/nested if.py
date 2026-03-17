#----------------find the num is above the teb-------------------
x = int(input("enter the num : "))

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#--------------Is he eligible for driving--------------------
age = input("enter the age : ")
has_license = input("has_license : ")

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

#---------------sumited assingment with good score --------------------
score = int(input("enter the num : "))
attendance = int(input("enter the num : "))
submitted = input("submitted: ")

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")
#----------------temperature-------------------

temperature = int(input("enter the temperature : "))
is_sunny =input("is_sunny : ")

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")
    
#shortland method-------------------------------
temperature = int(input("enter the temperature : "))
is_sunny = input("is_sunny : ")

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")


#----------------User login detail-------------------
username = input("enter username : ")
password = input("enter password : ")
is_active = input("is_active : ")

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")


#-------------Score result----------------------

score = int(input("enter the score : "))
extra_credit = int(input("enter the extra_credit : "))

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")  


























    









  
