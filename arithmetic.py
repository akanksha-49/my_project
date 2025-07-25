def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Give Correct Input"

print("Give The Inputs")
a = float(input("First Number: "))
b = float(input("Second Number: "))

print("Addition Of Numbers:", add(a, b))
print("Subtraction Of Numbers:", sub(a, b))
print("Multiplication of Numbers:", mul(a, b))
print("Division Of Numbers:", div(a, b))
