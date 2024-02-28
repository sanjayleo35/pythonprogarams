'''def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
print(factorial(5))  
print(factorial(0))  
print(factorial(-1)) 
'''



num = int(input("Enter a positive integer: "))

if num < 0:
    print("Error: Input must be a non-negative integer.")
elif num == 0 or num == 1:
    print(f"Factorial of {num} is 1")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial of {num} is {fact}")