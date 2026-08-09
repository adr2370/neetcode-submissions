class Solution:
    def isValid(self, s: str) -> bool:
        needed = []
        for c in s:
            if c == "(":
                needed.append(")")
            elif c == "{":
                needed.append("}")
            elif c == "[":
                needed.append("]")
            elif c == ")" or c == "}" or c == "]":
                if not needed or needed.pop() != c:
                    return False
        if needed:
            return False
        return True