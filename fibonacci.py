'''n = int(input("enter the number"))
num1 = 0
num2 = 1
next_number = num2 
count = 1

while count <= n:
	print(next_number, end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()'''


num = int(input("Enter a number: "))
a, b = 0, 1
sequence = []

while a < num:
    sequence.append(a)
    a, b = b, a + b

print(sequence)