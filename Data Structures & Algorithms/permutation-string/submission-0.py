class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def compareCounts(d1: Dict[string, int], d2: Dict[string, int]) -> bool:
            for key, value in d1.items():
                if value > 0 and d2.get(key, -1) != value:
                    return False
            for key, value in d2.items():
                if value > 0 and d1.get(key, -1) != value:
                    return False
            return True

        s1_counts = {}
        for c in s1:
            s1_counts[c] = s1_counts.get(c, 0) + 1
        running_counts = {}
        for i, c in enumerate(s2):
            if i >= len(s1):
                running_counts[s2[i-len(s1)]] -= 1
            running_counts[c] = running_counts.get(c, 0) + 1
            if compareCounts(s1_counts, running_counts):
                return True
        return False