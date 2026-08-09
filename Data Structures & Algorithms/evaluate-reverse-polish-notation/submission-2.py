class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        items = []
        for t in tokens:
            if t == "+":
                a, b = items.pop(), items.pop()
                items.append(b+a)
            elif t == "-":
                a, b = items.pop(), items.pop()
                items.append(b-a)
            elif t == "*":
                a, b = items.pop(), items.pop()
                items.append(b*a)
            elif t == "/":
                a, b = items.pop(), items.pop()
                items.append(int(b/a))
            else:
                items.append(int(t))
        return items[0]