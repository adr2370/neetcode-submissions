class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        tuples = []
        for key, value in counts.items():
            tuples.append((value, key))
        
        tuples.sort()
        
        output = []
        for _ in range(k):
            (_, v) = tuples.pop()
            output.append(v)
        return output