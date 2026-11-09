import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # yes
        # not a conflict to have same end/start points
        # 0 if array is empty
        # output: int

        # some meetings
        # up to meeting i, we require k rooms so far, and each room has a ending time

        # given a new meeting, we want to schedule our meeting st
        # 1. we want the best room st we dont have to make new rooms later
        
        # all end before the current meeting starts
        # when we choose our meeting room, we want to schedule it to the one that ends the earliest
        # only some of them
        # same heuristic as above
        # none of them end before the current meeting starts
        # we'll just create a new room 

        # min heap: contain values representing rooms, values are the ending time of the current meeting in that room 

        # intervals: [(0,40),(5,10),(15,20)]
        # h = [20, 40]

        # start: 15, end: 20

        h = []

        intervals = sorted(intervals, key = lambda intl: intl.start)

        # as we iterate thru our meetigs from earliest starting to latest starting
        for interval in intervals:
            start, end = interval.start, interval.end

            if len(h) == 0:
                heapq.heappush(h, end)
                continue

            if h[0] <= start:
                heapq.heappop(h)
                heapq.heappush(h, end)
            else:
                heapq.heappush(h, end)

        return len(h)
        # we check if the top elem (earliest ending time) <= current meeting start:
        # schedule it with this meeting
        # we'll pop the heap top, replace it with ending

        # make a new room, 
        # we'll push the end time of our current meeting to our heap