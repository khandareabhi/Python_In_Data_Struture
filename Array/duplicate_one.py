arr=[10,20,30,10,20]

seen=set()
duplicate=set()

for num in arr:
    
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)


print("duplicate element: ",duplicate)