from sortedcontainers import SortedList

class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = SortedList()
        self.map[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        index = self.map[key].bisect_left((timestamp,""))
        if index < len(self.map[key]) and self.map[key][index][0] == timestamp:
            return self.map[key][index][1]
        if index == 0:
            return ""
        return self.map[key][index - 1][1]
