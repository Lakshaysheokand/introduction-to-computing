#----------------------ASSIGNMENT START-----------------------#

print("ASSIGNMENT 1")
print()

#QUESTION 1

# TO FIND THE AVERAGE OF THREE NUMBERS

print("Question 1")
print("to find avgerage of three numbers")
print()
a=int(input("enter the first  number:"))    # FIRST  NUMBER
b=int(input("enter the second number:"))    # SECOND NUMBER
c=int(input("enter the third  number:"))    # THIRD  NUMBER
Average=(a+b+c)/3
print("The average of the given numbers is:-",Average)


#QUESTION 2

# TO FIND THE TAX
print()
print("Question 2")
print("to find the tax payable")
print()

gross_income = int(input("Enter your Gross Income in nearest integer :   "))
dependent =  int(input("Enter total number of dependents  :"))

dep_deduct =  dependent*3000
tax_rate=0.2
taxable_income = (gross_income) - (dep_deduct) - 10000

if taxable_income > 0:
    tax = taxable_income*tax_rate
    print("Total payable tax =  ",tax)
else:
    print("no tax for you")


#QUESTION 3

# TO START THE DATA OF STUDENTS INTO LIST

print()
print("to store the  data of students into list")
print(" Question - 3 ")

student_sid = int(input("Enter your sid     :  "))
name        = input("Enter your name        : ")
gender      = input(" Enter your gender ( F , M , U)  :")
Course_name = input("Enter your course name : ")
CGPA =  float(input("Enter your CGPA        : "))

data = [student_sid,name,gender,Course_name,CGPA]

print(data)


#QUESTION 4

# TO STORE THE STUDENTS MARKS IN A LIST IN A SORTED ORDER

print()
print("Question 4")
print("to store the students marks  in a list in a sorted  order")

a= int(input("Enter your first marks   : "))
b= int(input("Enter your second marks  : "))
c= int(input("Enter your third marks   : "))
d= int(input("Enter your fourth marks  : "))
e= int(input("Enter your fifth marks   : "))

marks=[a,b,c,d,e]

marks.sort()
print(marks)

#QUESTION 5

print()
print("Question 5 :  ")
print("Question related to list of colours")
print()


colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(" list provided ", colours)

# First Task

colours.pop(3)
print(" 1st question to remove 4th element ")
print(colours)


# Second Task
colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("2nd question  to  remove  Black and Pink  and change it to purple :  ")

#in one line
colours[3:4] = ["purple"]

print(colours)

#----------------------ASSIGNMENT OVER-----------------------#
