a=[23,25,26,27,28,29,30,31,32,33,34,35,36,37]
print(a)

target=int(input("Enter the number: "))

set_a=set(a)

if target in set_a:
    print("Target is matched",target,"at index",a.index(target))
else:
    print("Target not matched")