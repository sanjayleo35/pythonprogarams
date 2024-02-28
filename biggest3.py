'''BIGGEST AMONG FOUR NUMBERS'''
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=int(input("enter d"))
if(a<b or a<c or a<d):
    if(b<c or b<d) :
       if(c>d):
          print("c is big")
       else:
          print("d is big") 
    else:
        print("b is big")    
else:
    print("a is big")
