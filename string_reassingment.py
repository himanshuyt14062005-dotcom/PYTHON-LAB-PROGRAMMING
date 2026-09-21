def change_string(s):
	"""Try to replace the first character and return the reassigned string."""
	s = "X" + s[1:]
	return s


original = "hello"
changed = change_string(original)

print("Inside function result:", changed)
print("Original string:", original)
