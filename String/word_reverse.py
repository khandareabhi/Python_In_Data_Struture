s = "this is mmyself"

words=s.split() # this is spliting the s string in this 

result=[]

for word in words:
 result.append(word[::-1])


print(" ".join(result))


