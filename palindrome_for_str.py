string = input("Enter a string: ")

if len(string) == 0 or len(string) == 1:
    print(f"{string} is a palindrome.")
else:
    is_palindrome = True
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            is_palindrome = False
            break

    if is_palindrome:
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is not a palindrome.")