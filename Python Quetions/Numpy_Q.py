#NumPy Practical Test: Employee Data Analysis (Long Question)
#* Problem Statement

#You are given data of 8 employees in a company. Each row represents one employee, and the columns represent:

##Salary (₹)
##Experience (in years)
##Working Hours per week
##Performance Score (out of 100)
import numpy as np

data = np.array([
 [25000, 1, 40, 65],
 [40000, 3, 45, 78],
 [55000, 5, 50, 85],
 [30000, 2, 42, 70],
 [70000, 7, 55, 92],
 [45000, 4, 48, 80],
 [60000, 6, 52, 88],
 [28000, 1, 38, 60]
])
##Column Representation-------------------------------------:
##[Salary, Experience, Hours, Performance]
#🔹 Tasks###------------
## -------------------1.Basic Information-------------
##----------Print the shape, size, and number of dimensions of the array.----------

print(data.shape)
print(data.dtype)
print(data.ndim)

##-------------------2. Column Separation---------------
##Extract and store the following columns into separate variables:
##Salary
##Experience
##Working Hours
##Performance Score
#print(np.hsplit(data,4))

sal,exp,work,perf=np.array_split(data, 4,axis=1)

print(sal)
print(exp)
print(work)
print(perf)

#-------------------- 3.Salary Analysis---------------
##Calculate:
##Total salary payout
##Average salary
##Maximum salary
##Minimum salary

print("sum: ",np.sum(sal))
print("average: ",np.mean(sal))
print("max: ",np.max(sal))
print("min: ",np.min(sal))

## ---------------4. Performance Analysis--------------
##Find:
##Average performance score
##Number of employees with performance greater than 80

print("average: ",np.mean(perf))
num=perf[perf>80]
print("Number of employees with performance greater than 80: ",len(num))

##-------------------5. Experience-Based Filtering---------------
##Display the data of employees who have more than 3 years of experience.

filtered_data = data[data[:, 1] > 3]

print(filtered_data)

## ---------------6. Salary Increment (Broadcasting)-----------
##Increase each employee’s salary by 10% using NumPy broadcasting.

print("salary by 10% ",sal + sal*0.1)

##--------------7. Overtime Analysis------------------
##Identify employees who work more than 50 hours per week.

print("employees 50 hours",data[data[:,2]>50])

##---------------8. Performance Grading--------------------
##
##Assign grades based on performance:
##
##Grade A → Performance ≥ 85
##Grade B → Performance between 70 and 84
##Grade C → Performance < 70

grade=[]

for x in perf:
    if x >=85:
        grade.append("A")
    elif 70<x <84:
        grade.append("B")
    elif x <70:
        grade.append("C")
    else:
        grade.append("D")
print("grading by it's performance : ",grade)

##----------------------9. Correlation Analysis----------------
##Compute the correlation between salary and performance.
salary = data[:, 0]
performance = data[:, 3]

correlation = np.corrcoef(salary, performance)[0, 1]
print("Correlation:", correlation)

##--------------- 10. Top Performers----------------
##Identify the indices of the top 2 employees based on performance.

top2_indices = data[:, 3].argsort()[-2:][::-1]
print("top2_indices: ",top2_indices)

##print(np.sort(perf[-2]))

##----------------11. Sorting------------------------
##Sort the entire dataset in ascending order based on salary.

print("sorting by salary: ",np.sort(data,axis=1))#rearranges values

sorted_data = data[data[:, 0].argsort()]#rearranges rows based on a column

print("sorting by salary: ",sorted_data)

##-------------- 12. Combined Filtering-----------
##Display employees who satisfy both:
##Salary > 40000

##Performance > 80
empl=data[(data[:,0]>40000) & (data[:,3]>80)]
print("Salary and Performance: ",empl)

##------------------- 13. Normalization------------------
##Normalize the salary column to a range between 0 and 1.
Normalize=(sal - np.min(sal)) / (np.max(sal) - np.min(sal))

print("Normalize salary: ",Normalize)

##---------------------14. Efficiency Metric---------------
##
##Define efficiency as:
##
##Efficiency = Performance / Working Hours
##Calculate efficiency for each employee.

Efficiency=perf/work
print("Efficiency: ",Efficiency)

##--------------------15. Best Employee (Efficiency)---------------
##Find the index of the employee with the highest efficiency.

print("highest efficiency: ",np.max(Efficiency))

