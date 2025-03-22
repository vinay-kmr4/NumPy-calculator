# Step 1. Adding python library
import numpy as np

# Step 2. Arithematic operation
# Function like add, multiply, subtract, divide.

def add(a, b):
    return np.add(a, b)

def subtract(a, b):
    return np.subtract(a, b)

def multiply(a, b):
    return np.multiply(a, b)

def divide(a, b):
    try:
        return np.divide(a, b)
    except ZeroDivisionError:
        return "Error! Division by Zero"


# print("addition : ",add(3, 6))
# print("dividtion : ",divide(3, 2))
# print("multiply : ",multiply(5, 9))

# Step 3. Trignometric operations
# Functions like sin, cos , tan

def sin(angle):
    return np.sin(np.radians(angle))

def cos(angle):
    return np.cos(np.radians(angle))

def tan(angle):
    return np.tan(np.radians(angle))

# print(sin(90))
# print(tan(45))
# print(cos(90))

# Step 4: Logarithm & Exponent¶
# Functions for log, exponent, and power

def log(value, base=10):
    return np.log10(value) if base == 10 else np.log(value)

def exponent(value):    # e^0 = 1
    return np.exp(value)

def power(base, exp):
    return np.power(base, exp)


# print(log(8))
# print(exponent(0))
# print(power(2, 5))


# Step 5: Matrix Operations
# Matrix Addition, Multiplication, Transpose, and Determinant¶

def matrix_add(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def matrix_multiply(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def matrix_transpose(matrix1):
    return np.transpose(matrix1)

def matrix_determinent(matrix1):
    return np.linalg.det(matrix1)
    
# # simple matrix 3x3
# matrix = np.matrix([[1,2,3],
#                     [2,3,5],
#                     [2,6,4]])

# print(matrix_determinent(matrix))
# print(matrix_transpose(matrix))

# matrix2 = np.array([[2,3,4],
#                    [6,5,4],
#                    [3,7,9]])

# print(matrix_multiply(matrix, matrix2))


# Step 6: User Input and Menu for Calculator
# Menu and Input Handling¶

import numpy as np

def main_menu():
    print("\nhi... this is a numpy scientific calculation")
    print("1. Basic operations (+,-,*,/)")
    print("2. trignometric operations (sin, cos, tan)")
    print("3. logrithmic, exponent (log, exp, power)")
    print("4. matrix operations")
    print("5. Exit\n")


while True: 
    main_menu()

    choose = int(input("Enter your number from (1-5)"))

    if choose == 1:
        num1 = int(input("Enter your first number : "))
        num2 = int(input("Enter your second number : "))
        oprtor = input("Enter your operator : ")

        if oprtor == '+':
            print(np.add(num1, num2))
        elif oprtor == '-':
            print(np.subtract(num1, num2))
        elif oprtor == '*':
            print(np.multiply(num1, num2))
        elif oprtor == '/':
            try:
                 print(np.divide(num1, num2))
            except ZeroDivisionError:
                print("Error ! Division by zero")
        else:
            print("Invalid operator")

    elif choose == 2:
        sign = input("Enter your (sin, cos, tan) value : ")
        angle = int(input("Enter your angle : "))

        if sign == 'sin':
            print(np.sin(np.radians(angle)))
        elif sign == 'cos':
            print(np.cos(np.radians(angle)))
        elif sign == 'tan':
            print(np.tan(np.radians(angle)))
        else :
            print("Invalid sign value")

    elif choose == 3:
        var = input("choose one (log, exp, power) : ")
        val = int(input("Enter your value : "))

        if var == 'log':
            print( np.log10(val))
        elif var == 'exp':
            print( np.exp(val))
        elif var == 'power':
            base = int(input("Enter your base value : "))
            print( np.power(base, val))
        else :
            print( "Invalid input")
    
    elif choose == 4: 
        matrix1 = np.array([[int(input("Enter your matrix 1 elements [[]] : ".format(i, j))) for j in range(2)] for i in range(2)])
        mat_op = input("Enter your matrix operation (add, multipy, transpose, determenent) : ")

        if mat_op == 'add':
            matrix2 = np.array([[int(input("Enter your matrix 2 elements [[]] : ".format(i, j))) for j in range(2)] for i in range(2)])
            print( np.add(matrix1, matrix2))
        elif mat_op == 'multiple':
            matrix2 = np.array([[int(input("Enter your matrix 2 elements [[]] : ".format(i, j))) for j in range(2)] for i in range(2)])
            print( np.dot(matrix1, matrix2))
        elif mat_op == 'transpose':
            print( np.transpose(matrix1))
        elif mat_op == 'determenet':
            print( np.linalg.det(matrix1))
        else:
            print( "Invalid matrix operation")

    elif choose == 5:
        print("bye bye")
        break
    else:
         print("Enter your valid number okay bro..")