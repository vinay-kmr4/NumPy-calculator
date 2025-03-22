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


print("addition : ",add(3, 6))
print("dividtion : ",divide(3, 2))
print("multiply : ",multiply(5, 9))