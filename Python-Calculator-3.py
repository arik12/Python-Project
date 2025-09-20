
# -----------------------------------
# Simple Python Calculator using Functions
# -----------------------------------

# Define functions for each operation
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    # Handle division by zero
    if num2 == 0:
        return "Error: Division by zero!"
    else:
        return num1 / num2

# Print headline
print("|Python-Calculator!!!|")
print("Operations: (+ , - , * , /)\n")

# Take input from the user
num1 = int(input("Enter First Number: "))
op = input("Enter operator (+ , - , * , /): ")
num2 = int(input("Enter Second Number: "))

# Perform calculation based on operator
if op == "+":
    result = add(num1, num2)
elif op == "-":
    result = sub(num1, num2)
elif op == "*":
    result = mul(num1, num2)
elif op == "/":
    result = div(num1, num2)
else:
    result = "Invalid Operator!"

# Display the result
print(f"Result: {num1} {op} {num2} = {result}")
