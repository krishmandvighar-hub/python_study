print("sales report")
sales_man_name =input("enter your name")
print(sales_man_name)
jan =int(input("enter the sales in january: "))
feb =int(input("enter the sales in february: "))
mar =int(input("enter the sales in march: "))
Apr =int(input("enter the sales in april: "))
total =(jan +feb + mar +Apr)
Ave =total/4
print("total sales", total)
print("Average sales", Ave)

if Ave>1000:
    print(Ave,"is good sales")
    
else:
    print(Ave,"must improve the sales")
