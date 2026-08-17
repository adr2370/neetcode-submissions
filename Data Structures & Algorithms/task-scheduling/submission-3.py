class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        freq = {}
        for t in tasks:
            freq[t] = 1 + freq.get(t, 0)
        v = [-f for f in freq.values()]
        
        def help(v, total):
            m = -min(v)
            max_count = 0
            for f in v:
                if -f == m:
                    max_count += 1
            required = (m - 1) * (n + 1) + max_count
            if required >= total:
                return required
            for i in range(required):
                c = heapq.heappop(v)
                if c < -1:
                    heapq.heappush(v, c + 1)
            return required + help(v, total - required)

        return help(v, len(tasks))