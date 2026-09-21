def add_entry(d):
	"""Mutate the original dictionary by adding a key-value pair."""
	d["new_key"] = "new_value"


def reassign_dict(d):
	"""Rebind only the local variable to a new dictionary."""
	d = {"replacement_key": "replacement_value"}


data = {"name": "Alice"}

print("Before add_entry:", data)
add_entry(data)
print("After add_entry:", data)

reassign_dict(data)
print("After reassign_dict:", data)
 