# TASK :-CALCULATOR

'''Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.'''


'''In my opnion,here it is a short and concise algorithm which easily to learning up to the implementation of code for the calculator program in python.'''
# STEP 1:-Start the program
# STEP 2:-Take two numbers as user input using the input function
# STEP 3:-Take the operation to be performed using the input function
# STEP 4:-'''Use conditional logic,
#                               if-else to select the operation to perform on the two operands.'''
# STEP 4.1:-If the elements and operators in if else condition where operation is available then it execute by operating which operate apply in two operands(+,-,*,/,%)
# STEP 4.1.1:-else show Invaild Input commands
# STEP 5:-Store the computed value in an object named result.
# STEP 6:-Print the result.
# STEP 7:-End the program.

# CODE:-

p = int(input("Enter the first input: "))
q = int(input("Enter the second input: "))

oper = input("Enter the type of operation you want to perform (+, -, *, /, %): ")

result = 0
if oper == "+":
    result = p+q
elif oper == "-":
    result = p-q
elif oper == "*":
    result = p*q
elif oper == "/":
    result = p//q
elif oper == "%":
    result = p%q
else:
    print("Invalid Input")
print("Your answer is: ",result)