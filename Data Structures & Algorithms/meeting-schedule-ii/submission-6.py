"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # find the min number of rooms to schedule all meetings without conflicts 
        # calculate # arrays we need, so that the meeting times 
        # in each of the array are non-overlapping 
        # keep n arrays, times in each of which the array is over-lapping 
        # min(n); start = end x conflict 
        # ori_array, when we find a time conflict -> create array 2, put it there 
        # when we find another time conflict, and cannot fit it into array 2 
        # array 3 ... 

        # max rooms we need = max of meeting in same point of time (peak time)
        # sort the array, ascending start time 
        # end[i - 1] < start[i] -> overlap, 
        # increment the # rooms, and keep the overlapping period 
        # if there's another collision with the overlapping period, increment 

        # keep track of the earliest end using heap 
        leng = len(intervals)
        if leng == 0 or leng == 1: 
            return leng
        intervals.sort(key = lambda x: x.start)
        endingTime = [] 
        heapq.heappush(endingTime, intervals[0].end)
        res = 1 
        for i in range(1, leng): 
            # print(intervals[i].start, intervals[i].end)
            end = endingTime[0]
            # print(f"earliest end {end}")
            if end > intervals[i].start:
                res += 1 
                # print("another room")
            else: 
                heapq.heappop(endingTime)
            heapq.heappush(endingTime, intervals[i].end)
        return res 

            

