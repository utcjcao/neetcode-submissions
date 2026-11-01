import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.user_to_following = defaultdict(set)
        self.user_to_tweets = defaultdict(list)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets[userId].append((self.t, tweetId))
        self.t -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        for i, following in enumerate(self.user_to_following[userId]):
            for time, tweet in self.user_to_tweets[following]:
                heapq.heappush(h, (time, tweet))
        
        for time, tweet in self.user_to_tweets[userId]:
            heapq.heappush(h, (time, tweet))

        ans = []
        while len(h) > 0 and len(ans) < 10:
            time, tweet = heapq.heappop(h)
            ans.append(tweet)
        
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_to_following[followerId]:
            self.user_to_following[followerId].remove(followeeId)

        
