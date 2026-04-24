#1.write a function that counts how many sales values are greater than a given target value.

def fun(target,*sales):
    count=0
    good_sales=[]
    for x in sales:
        if x > target:
            count+=1
            good_sales.append(x)
    print("highest sales value count: ",count)
    print("good sales: ",good_sales)
fun(5000,9000,7000,2000,3000,5500)

#2.write a function that return the product name having the highest sales value.


def pro(**sale):
        
    for key, val in sale.items():
        MaxVal = max(sale.values())
        if MaxVal == sale[key]:
            print("Highest sales Product name:", key)
        
pro(computer=40000,labtop=25000,smart_TV=15000,AC=50000)    
    
#3.write a function that return the expense category having the lowest amount.

def exp(**amount):
        
    for key, val in amount.items():
        MinVal = min(amount.values())
        if MinVal == amount[key]:
            print("The lowest amount: ", key,"=",val)
        
exp(diamond=400000,silver=25000,alluminium=15000,graphite=10000)

#4.write a function that returns a dictionary where each student is marked as "pass" if marks>= 40,
#otherwise "fail"

def stma(**studmark):
    for x,y in studmark.items():
        if y>=40:
            studmark[x]= "pass" 
        else:
            studmark[x]= "fail" 
    print(studmark)

stma(rumana=90,krishna=39,latron=91,kartik=22,sumit=35,snedan=96)

#5.write a function that return employee names who worked more than 10 overtime hours.

employee_names=[]
def work(**empl):
    for x,y in empl.items():
        if y>10:
            employee_names.append(x)
    print("employee_names: ",employee_names)       
work(ramesh=7,rakesh=6,sandeep=8,manish=10,kartikey=15,pilot=18,shushmit=17,AI=24)

#6.write a function return employees eligible for promotion.
#(condition:performance score>=8 and experience >=3.)


permotionUser= []

def emplo(**emp):
    for x,obj in emp.items():
        if obj["score"]>=8 and  obj["exp"]>=3:
            permotionUser.append(x)
    print("permotion list : ", permotionUser)   

emplo(kris=
      {"score": 5, "exp": 4},
        flewing=
      {"score": 9, "exp": 4},
        rakesh=
      {"score": 9, "exp": 6},
        praksh=
      {"score": 2, "exp": 2})

    
