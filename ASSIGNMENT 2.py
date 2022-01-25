print("----------------------------------ASSIGNMENT 2-----------------------------")

print('-------------------------------Question #1----------------------------------')

# giving value to input_string.
input_string = 'Python is a case sensitive language'

# printing the length of input_string.
print("\nPart a ")
print(f"Length of Input String = {len(input_string)}")

# printing the input_string in reverse order.
print("\nPart b")
print(input_string[::-1])


# slicing and printing the input_string.
print("\nPart c")
sliced_string = input_string[10:26]
print(sliced_string)
print


# replacing and printing.
print("\nPart d")
new_string = input_string.replace("a case sensitive", "object oriented")
print(new_string)


# printing index of "a" from input_string.
print("\nPart e")
print(input_string.index("a"))


# replacing blank white spaces with empty string.
print("\nPart f")
print(input_string.replace(" ", ""))
print("")

####################################################################################

print("---------------------------------Question #2----------------------------------")
print(" ")
print("TO PRINT A STATEMENT IN GIVEN FORMAT.")
print(" ")
# Initializing variables.
Name = "Lakshay Sheokand"
SID = "21105046"
Department_name = "ECE"
CGPA = "10"

# Printing statements in the given format.
print(f" Hey, {Name.title()} here! \n My SID is {SID} \n I am from {Department_name} and my CGPA is {CGPA}")
print("")

#####################################################################################

print("---------------------------------Question #3----------------------------------")
print(" ")
print("TO CALCULATE THE FOLLOWING USING BITWISE OPERATORS.")
print(" ")
a = 56
b = 10
print(" a&b : ", a & b)
print(" a|b : ", a | b)
print(" a^b : ", a ^ b)

# Left shift both a and b with 2 bits.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)
# Right shift a with 2 bits and b with 4 bits.
print("a>>2 : ", a >> 2, "\tb>>2 :", b >> 4)
print("")

###################################################################################

print("---------------------------------Question #4----------------------------------")
print(" ")
print("TO DETERMINE THE GREATEST NUMBER OF ALL THREE NUMBERS.")
print(" ")
a = int(input("Enter the first number :- "))
b = int(input("Enter the second number:- "))
c = int(input("Enter the third number :- "))

#Detrmining the greatest number
if a > b:
    if a > c:
        highestnumber = a
    else:
        highestnumber = c

if b > a:
    if b > c:
        highestnumber = b
    else:
        highestnumber = c


print(f"Greatestnumber = {highestnumber}")
print("")

#####################################################################################

print("---------------------------------QUESTION #5----------------------------------")
print(" ")
print("TO CHECK IF THE WORD name IS PRESENT IN THE STRING ")
print(" ")
String = input("Enter the string:- ")
if "name" in String:
    print("Yes,name is there.")
else:
    print("No,name is not there.")
print(" ")
print(" ")

#####################################################################################

print("----------------------------------QUESTION #6---------------------------------")
print(" ")
print("TO FIND IF THE TRIANGLE IS POSSIBLE OR NOT ")
print(" ")
Side_1 = int(input("Enter the FIRST side of the triangle:- "))
Side_2 = int(input("Enter the SECOND side of the triangle:- "))
Side_3 = int(input("Enter the THIRD side of the triangle:- "))         
print(" ")
if Side_1+Side_2 > Side_3 and Side_2+Side_3 > Side_1 and Side_1+Side_3 > Side_2:
        print("YES,THE TRIANGLE IS POSSIBLE")
else:
        print("NO, THIS TRIANGLE IS NOT POSSIBLE")
print("")

 ####################################################################################       

print("----------------------------------ASSIGNMENT OVER-----------------------------")
          
