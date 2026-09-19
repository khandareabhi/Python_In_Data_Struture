arr=[10,20,30,40,50,5]

even=0
odd=0

for i in arr:
    if(i % 2==0):
        even=even+1
    if(i %2==1):
        odd=odd+1


print("Sum of the odd: ",odd)
print("Sum of the even: ",even)