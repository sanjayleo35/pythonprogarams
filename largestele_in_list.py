lst = input("Enter a list of numbers separated by spaces: ").split()
lst = [int(i) for i in lst]

if not lst:
    print("Error: Input list cannot be empty.")
else:
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
    print("Largest element in the list:", largest)