def remove_last(lst):
	"""Remove and return the last element of lst."""
	return lst.pop()


numbers = [1, 2, 3, 4]
removed = remove_last(numbers)

print("Removed:", removed)
print("Original list after function call:", numbers)
