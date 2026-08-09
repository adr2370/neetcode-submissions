class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = []
        for character in s:
            c = ord(character)
            if c >= ord('A') and c <= ord('Z'):
                newS.append(c - ord('A'))
            elif c >= ord('a') and c <= ord('z'):
                newS.append(c - ord('a'))
            elif c >= ord('0') and c <= ord('9'):
                newS.append(c)
        start, end = 0, len(newS) - 1
        while end > start:
            if newS[start] != newS[end]:
                return False
            start += 1
            end -= 1
        return True