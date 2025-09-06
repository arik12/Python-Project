
# -----------------------------------
# Simple Python Calculator using List
# -----------------------------------

# Print a headline
print("|Python-Calculator!!!|")

# Show available operations
print("Operations: (+ , - , * , /)\n")

# Initialize a list to store: [first number, operator, second number]
data = [0, "", 0]

# Take input for the first number
data[0] = int(input("Enter First Number: ")) 

# Take input for the operator (+, -, *, /)
data[1] = input("Enter operator (+ , - , * , /): ")

# Take input for the second number
data[2] = int(input("Enter Second Number: ")) 

# Perform calculation based on operator
if data[1] == "+":
    result = data[0] + data[2]           # Addition
elif data[1] == "-":
    result = data[0] - data[2]           # Subtraction
elif data[1] == "*":
    result = data[0] * data[2]           # Multiplication
elif data[1] == "/":
    if data[2] != 0:
        result = data[0] / data[2]       # Division (with zero check)
    else:
        result = "Error: Division by zero!"
else:
    result = "Invalid operator!"         # If operator is not recognized

# Display the result
print(f"Result: {data[0]} {data[1]} {data[2]} = {result}")
