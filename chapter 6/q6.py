marks = int(input("enter the marks : "))

if(marks<=100 and marks>=90):
    grade = "ex"

elif(marks<=90 and marks>=80):
    grade = "A"

elif(marks<=80 and marks>=70):
    grade = "B"

elif(marks<=70 and marks>=60):
    grade = "C"

elif(marks<=60 and marks>=50):
    grade = "D"

else:
    grade = "fail"

print("your grade is : ", grade)