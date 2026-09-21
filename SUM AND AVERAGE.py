user_input = []
print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    user_input.append(num)

# Calculate sum
total = sum(user_input)
print(f"Sum: {total}")

# Calculate average without using sum
average = total / len(user_input)
print(f"Average: {average}")

