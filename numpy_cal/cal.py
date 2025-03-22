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

# Step 3. Trignometric operations
# Functions like sin, cos , tan

def sin(angle):
    return np.sin(np.radians(angle))

def cos(angle):
    return np.cos(np.radians(angle))

def tan(angle):
    return np.tan(np.radians(angle))

print(sin(90))
print(tan(45))
print(cos(90))

# Step 4: Logarithm & Exponent¶
# Functions for log, exponent, and power

def log(value, base=10):
    return np.log10(value) if base == 10 else np.log(value)

def exponent(value):    # e^0 = 1
    return np.exp(value)

def power(base, exp):
    return np.power(base, exp)


print(log(8))
print(exponent(0))
print(power(2, 5))