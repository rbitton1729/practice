# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Ask the user for two numbers
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

# Add the numbers using the function
result = add_numbers(a, b)

# Display the result
print(f"The sum of {a} and {b} is {result}.")
