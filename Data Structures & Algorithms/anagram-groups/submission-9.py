class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def charCount(s: str) -> str:
            counts = defaultdict(int)
            for c in s:
                counts[c] += 1
            countTuples = []
            for key, value in counts.items():
                countTuples.append((key, value))
            countTuples.sort()
            output = ""
            for (key, value) in countTuples:
                output = f"{output}{key}{value}"
            return output
        
        anagrams = []
        for str in strs:
            currCount = charCount(str)
            anagrams.append((currCount, str))
        anagrams.sort()

        output = []
        lastCount = "-1"
        for (count, str) in anagrams:
            if count != lastCount:
                output.append([str])
            else:
                output[len(output)-1].append(str)
            lastCount = count
        return output

