class Cola:

    def new(self):
        self.cola=[]
    
    def enqueue(self,x):
        self.cola.append(x)

    def dequeue(self):
        #try:
            return self.cola.pop(0)
        #except:
            #raise ValueError("La cola está vacía")


    def isEmpty(self):
        return self.cola == []

    def size(self):
        return len(self.cola)
