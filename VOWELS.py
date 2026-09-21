a=(input("Enter a string: "));
print("UPPER CASE: ", a.upper());
print("LOWER CASE: ", a.lower());
print("REVERSED: ", a[::-1]);
VOWELS = "AEIOUaeiou"
vowel_count = sum(1 for char in a if char in VOWELS)
print("VOWEL COUNT: ", vowel_count)