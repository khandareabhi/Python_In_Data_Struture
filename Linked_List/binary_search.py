a=[3,4,5,6,7,8,20,25]

target=20

low=0
high=len(a)-1

while low<=high:
    mid=(low+high)//2

    if a[mid]==target:
        print("Target found at index:",mid)
        break
    elif a[mid]<target:
        low=mid+1
    else:
        high=mid-1 # logic



    
