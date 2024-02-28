n=int(input("hoe many times you want check"))
for i in range(0,n):
    a=int(input("enter the value of A"))
    if(a<0):
        print("a is negative")
    elif(a>0):
        print("a is positive")
    else:
        print("invalid number")
    
