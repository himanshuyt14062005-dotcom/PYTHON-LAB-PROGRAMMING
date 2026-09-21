# Input a list from user and reverse it without using reverse() or slicing
user_input = input("Enter a list of elements separated by spaces: ")
lst = user_input.split()

print("Original list:", lst)

# Reverse the list without using reverse() or slicing
for i in range(len(lst) // 2):
    lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]

print("Reversed list:", lst)
