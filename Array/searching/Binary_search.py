arr=[12,2,3,5,6,78,8,90]

target =int(input("Enter the number: "))

low=0
high=len(arr)-1

while low<=high:
    mid=(low+high)//2
    if(arr[mid]==target):
        print("Target is matched",target,"at index",mid)
        break
    elif(arr[mid]<target):
        low=mid+1
    else:
        high=mid-1
else:
    print("Target not matched")