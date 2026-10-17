arr=[23,12,3,5,45,6]

target =int(input("Enter the number: "))

for num in arr:
    if(num==target):
        print("Target is matched",target)
        break
else:
    print("Target not matched")