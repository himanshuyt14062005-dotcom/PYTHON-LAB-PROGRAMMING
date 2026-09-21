def maximum(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum:", maximum(a, b))
