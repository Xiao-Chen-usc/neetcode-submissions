class DynamicArray:
    
    def __init__(self, capacity: int):
        self.stack = []
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.stack[i]


    def set(self, i: int, n: int) -> None:
        self.stack[i] = n


    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()
        self.stack.append(n)


    def popback(self) -> int:
        return self.stack.pop()
 

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return len(self.stack)
        
    
    def getCapacity(self) -> int:
        return self.capacity
