def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
n = int(input("Enter a number: "))
print("Factorial:", factorial(n))
