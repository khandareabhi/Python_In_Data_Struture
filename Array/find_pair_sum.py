arr= [10,20,40,50,10c]

target=30

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==target):
            print(arr[i],"+",arr[j],"=",target)