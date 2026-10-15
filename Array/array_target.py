arr=[1,2,3,4,5,6,56]

target=4

for i in range(len(arr)):
    if arr[i]==target:
        print("Target found at index:",i)
        break