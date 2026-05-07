# Factorial program in Python

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"Factorial of {num} is 1")
else:
    for i in range(2, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")