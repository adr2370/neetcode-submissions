class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1
        
        s_counts = {}
        required = len(t_counts)
        formed = 0
        start = 0
        shortest_start, shortest_end = -1, -1
        for i, c in enumerate(s):
            s_counts[c] = s_counts.get(c, 0) + 1
            if c in t_counts and s_counts[c] == t_counts[c]:
                formed += 1
            
            while formed == required:
                if shortest_end == -1 or shortest_end - shortest_start > i - start:
                    shortest_start, shortest_end = start, i
                
                left_char = s[start]
                s_counts[left_char] -= 1
                if left_char in t_counts and s_counts[left_char] < t_counts[left_char]:
                    formed -= 1
                start += 1

        if shortest_end == -1:
            return ""
        return s[shortest_start:shortest_end+1]