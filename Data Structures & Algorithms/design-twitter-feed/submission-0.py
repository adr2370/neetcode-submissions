class Twitter:

    def __init__(self):
        self.tweets = []
        self.tweet_time = 0
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, (self.tweet_time, userId, tweetId))
        self.tweet_time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        add_back = []
        follows = self.follows[userId] if userId in self.follows else set()
        follows.add(userId)
        while len(ans) < 10:
            if len(self.tweets) == 0:
                break
            n = heapq.heappop(self.tweets)
            add_back.append(n)
            if n[1] in follows:
                ans.append(n[2])
        for a in add_back:
            heapq.heappush(self.tweets, a)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)
        
