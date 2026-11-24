arr = [20,30,50,60,40]

search=500
found=False

for i in arr:
    if(i==search): # searching the element in the array
        found=True

if(found):
    print("Element is searched")

else:
    print("Element is not searched")