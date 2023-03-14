#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#

# @lc code=start
from typing import List
import time

class Twitter:

    def __init__(self):
        self.post = [[] for _ in range(501)]
        self.fo = [[_] for _ in range(501)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        t = time.time()
        self.post[userId].append((tweetId, t))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for id in self.fo[userId]:
            res += self.post[id]
        res.sort(reverse=True, key=lambda x:x[1])
        return [v[0] for v in res][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.fo[followerId].count(followeeId):
            self.fo[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.fo[followerId].count(followeeId):
            self.fo[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

