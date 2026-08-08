class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def countChar(s: str) -> List[str]:
            counts = defaultdict(int)
            for c in s:
                counts[c] += 1
            return counts
        return countChar(s) == countChar(t)