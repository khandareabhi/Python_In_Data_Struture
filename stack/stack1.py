stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print(stack)

stack.pop()
stack.pop()

print(stack)

print(stack[::-1]) # get the last element in this for the easy way in this for the improvement in this 

if len(stack)==0:
    print("Empty stack")
else:
    print("Not Empty")

print(stack[::-1])
