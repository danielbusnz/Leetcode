class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x:x[1])
        arrows = 1
        current_arrow = points[0][1]

        for start, end in points:
            if start > current_arrow:
                arrows += 1
                current_arrow = end
        return arrows