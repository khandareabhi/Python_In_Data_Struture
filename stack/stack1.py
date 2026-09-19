stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

stack.pop()

print(stack)

print(stack[::-1])

if len(stack)==0:
    print("Empty stack")
else:
    print("Not Empty")

print(stack[::-1])