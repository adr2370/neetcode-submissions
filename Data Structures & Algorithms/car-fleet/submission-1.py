class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        n = len(position)
        for i in range(n):
            cars.append((position[i], speed[i]))
        cars.sort()
        fleets = 1
        end_time = float(target - cars[-1][0]) / cars[-1][1]
        for i in range(n-1, -1, -1):
            (p, s) = cars[i]
            e = float(target - p) / s
            if e > end_time + 0.000001:
                fleets += 1
                end_time = e
        return fleets
