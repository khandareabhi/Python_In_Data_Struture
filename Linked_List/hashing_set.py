arr=[1,2,3,5,67,89,90,100]
seen=set(arr)
target=int(input("Enter the target value:"))
if target in seen:
    print("Target found",arr.index(target))
else:
    print("Target not found")