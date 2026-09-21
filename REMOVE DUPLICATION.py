def remove_duplicates():
    n = int(input("Enter the number of integers: "))
    numbers = []
    
    for i in range(n):
        num = int(input(f"Enter integer {i+1}: "))
        numbers.append(num)
   
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    print("Original list:", numbers)
    print("List without duplicates:", result)

if __name__ == "__main__":
    remove_duplicates()
