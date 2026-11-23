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
            

    