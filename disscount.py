# input sale amount
amt = int(input("Enter Sale Amount: "))

# checking conditions and calculating discount
if(amt>0):
    if amt<=5000:
       disc = amt-100
    elif amt<=15000:
        disc=amt-250
    elif amt<=25000:
        disc=500-amt
  #  else:
     #    disc=0.3 * amt

    print("Discount : ",disc)
    print("Net Pay  : ",amt-disc)
#else:
  #  print("Invalid Amount")
