class TimeMap:

    def __init__(self):
        self.d = {}

        # pretty clear that we are sorting with the timestamp values, b/c
        # the other two are static and unordered
        # the sets timestamps are strictly increasing, so we know that we can just append on top
        # but while bin search, we look for a specific value, we just need a value such that
        # there are a minimal number of elements beneath it
        # okay so it feels like a traditional search
        # when would we know if there are no possible values?
        # if time_stamp < first time_stamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        if self.d[key][0][0] > timestamp:
            return ""
        if timestamp >= self.d[key][-1][0]:
            return self.d[key][-1][1]
        l, r = 0, len(self.d[key])-1
        # 10 20 30, looking for 25
        # 1, 3, looking for 3
        # what are we actually looking for? i think we are looking for
        # the interval such that x <= target < y
        
        while r-l > 1:
            m = (l+r)//2
            if (self.d[key][m][0] < timestamp):
                if (r-m) > 1:
                    l = m+1
                else:
                    l = m
            elif (timestamp < self.d[key][m][0]):
                if (m-l) > 1:
                    r = m-1
                else:
                    r = m
            else:
                return self.d[key][m][1]
        return self.d[key][l][1]
            