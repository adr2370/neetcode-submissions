class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validSpeed(speed: int) -> bool:
            t = 0
            for p in piles:
                t += p // speed
                if p % speed > 0:
                    t += 1
            return t <= h

        s, e = 1, 1000000000
        min_end = 1000000000
        while s <= e:
            m = (s + e) // 2
            if validSpeed(m):
                min_end = min(min_end, m)
                e = m - 1
            else:
                s = m + 1
        return s