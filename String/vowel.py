s= "Programing"

count=0
for i in s:
    if i.lower() in 'aeiou':
        count=count+1



print("vowels: ",count)