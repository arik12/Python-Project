
# Designed Headline

print("|Python-Calculator!!!|")

# Available Operations
print("Operations:(+ , - , * , /)\n")

# Input
num1 = int(input("Enter first number: "))
operator = input("Enter operator (+ , - , * , /): ")
num2 = int(input("Enter second number: "))

# Processing
if operator == '+':
    result = num1 + num2

elif operator == '-':
    result = num1 - num2

elif operator == '*':
    result = num1 * num2

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"

else:
    result = "Invalid operator!"

# Output
print(f"Result: {num1} {operator} {num2} = {result}")
