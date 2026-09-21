numbers = []
for i in range(7):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
