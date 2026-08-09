class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        startIndex = 0
        replacements_needed = 0
        current_counts = defaultdict(int)
        running_max = 0
        for i, c in enumerate(s):
            current_counts[c] += 1
            max_count = max(current_counts.values())
            replacements_needed = sum(current_counts.values()) - max_count
            while replacements_needed > k:
                current_counts[s[startIndex]] -= 1
                startIndex += 1
                max_count = max(current_counts.values())
                replacements_needed = sum(current_counts.values()) - max_count
            running_max = max(running_max, i - startIndex + 1)
        return running_max
            
