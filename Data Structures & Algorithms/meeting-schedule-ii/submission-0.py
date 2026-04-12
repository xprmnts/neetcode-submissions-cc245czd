"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        res = rooms = 0
        s = e = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            res = max(res, rooms)
        
        return res