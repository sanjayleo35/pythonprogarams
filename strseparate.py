'''myStr=input("Enter string: ")
output=list(myStr)
print("The output is:",output)'''

input_str = input("Enter the String: ")
output = []

for i in range(len(input_str)):
    output.append(input_str[i])

print("The output is:", output)