import json

x =  '{ "name":"ajay", "age":22, "city":"Mumbai"}'

y = json.loads(x)
print(y)
print("I am",y["name"],".")
print("I am",y["age"],"years old.")
print("I lived in",y["city"],".")
#-----------------------------------------------
import json

x = {
  "Name": "Aajay",
  "Age": 22,
  "Married": False,
  "Indian": True,
  "Skills": ("Java","Python","C+& C++"),
  "Master done" : None,
  "Cars collection": [
    {"model": "BMW 230", "price": "1Cr"},
    {"model": "Tesla", "price": "5Cr"}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys = True ))




