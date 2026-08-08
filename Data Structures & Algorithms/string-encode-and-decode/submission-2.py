class Solution:

    def encode(self, strs: List[str]) -> str:
        str = ""
        for s in strs:
            str = f"{str}{len(s)}\\{s}"
        return str
    def decode(self, s: str) -> List[str]:
        output = []
        while len(s) > 0:
            index = s.find("\\")
            length = int(s[:index])
            s = s[index + 1:]
            output.append(s[:length])
            s = s[length:]
        return output
