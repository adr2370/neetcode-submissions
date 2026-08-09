class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.minStack:
            m = min(self.minStack[-1], val)
        else:
            m = val
        self.minStack.append(m)
        self.stack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
