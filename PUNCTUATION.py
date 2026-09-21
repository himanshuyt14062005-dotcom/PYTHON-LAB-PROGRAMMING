import string
text = input("Enter a string: ")
cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
print("string without punctuation: ", cleaned_text)