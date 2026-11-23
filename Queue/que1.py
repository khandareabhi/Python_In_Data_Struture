class queue:
    def __init__(self):
        self.values=[]

    def enqueue(self,value):
        self.values.append(value)

    def dequeue(self):
        if len(self.values)==0:
            return None
        else:
            return self.values.pop(0)



q1=queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

print(q1.dequeue())

print(q1.values)

