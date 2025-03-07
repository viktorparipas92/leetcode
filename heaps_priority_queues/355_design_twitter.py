"""
355. Design Twitter
-------------------
Difficulty: Medium

Implement a simplified version of Twitter which allows users to post tweets,
follow/unfollow each other, and view the 10 most recent tweets within their
own news feed.
Users and tweets are uniquely identified by their IDs (integers).

Implement the following methods:
- Twitter() Initializes the twitter object.
- void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the
  user userId. You may assume that each tweetId is unique.
- List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs
  in the user's news feed. Each item must be posted by users who the user is
  following or by the user themself. Tweets IDs should be ordered from most recent to
  least recent.
- void follow(int followerId, int followeeId) The user with ID followerId follows the
  user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId unfollows
  the user with ID followeeId.

Example 1:
Input:
['Twitter', 'postTweet', [1, 10], 'postTweet', [2, 20], 'getNewsFeed', [1], 'getNewsFeed', [2], 'follow', [1, 2], 'getNewsFeed', [1], 'getNewsFeed', [2], 'unfollow', [1, 2], 'getNewsFeed', [1]]

Output:
[null, null, null, [10], [20], null, [20, 10], [20], null, [10]]

Explanation:
Twitter twitter = new Twitter();
twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
twitter.getNewsFeed(1);   // only contain their own tweets -> [10].
twitter.getNewsFeed(2);   // only contain their own tweets -> [20].
twitter.follow(1, 2);     // User 1 follows user 2.
twitter.getNewsFeed(1);   // contain both tweets from user 1 and user 2 -> [20, 10].
twitter.getNewsFeed(2);   // only contain their own tweets -> [20].
twitter.unfollow(1, 2);   // User 1 follows user 2.
twitter.getNewsFeed(1);   // only contain their own tweets -> [10].

Constraints:
1 <= userId, followerId, followeeId <= 100
0 <= tweetId <= 1000
"""
from collections import defaultdict


class Twitter:
    """
    Time complexity: O(1) for all methods unless otherwise stated
    Space complexity: O(N * (m+M)), where
    - N is the number of users
    - m is the maximum number of tweets per user
    - M is the maximum number of followees per user
    """

    def __init__(self):
        self.time = 0
        self.follow_map: dict[int, set] = defaultdict(set)
        self.tweet_map: dict[int, list] = defaultdict(list)

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.tweet_map[user_id].append((self.time, tweet_id))
        self.time += 1

    def get_news_feed(self, user_id: int) -> list[int]:
        """
        Time complexity: O(n * m + t * log(t)), where
        - n is the number of followees of the user
        - m is the maximum number of tweets per user
        - t is the total number of tweets from the user and their followees
        """
        feed: list = self.tweet_map[user_id][:]
        for followee_id in self.follow_map[user_id]:
            feed.extend(self.tweet_map[followee_id])

        feed.sort(key=lambda x: -x[0])
        return [tweet_id for _, tweet_id in feed[:10]]

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id != followee_id:
            self.follow_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.follow_map[follower_id].discard(followee_id)


def test_twitter():
    solutions = [
        Twitter,
    ]

    for solution in solutions:
        # Arrange
        twitter = solution()

        # Act, Assert
        twitter.post_tweet(1, 10)
        twitter.post_tweet(2, 20)
        assert twitter.get_news_feed(1) == [10]
        assert twitter.get_news_feed(2) == [20]

        twitter.follow(1, 2)
        assert twitter.get_news_feed(1) == [20, 10]
        assert twitter.get_news_feed(2) == [20]

        twitter.unfollow(1, 2)
        assert twitter.get_news_feed(1) == [10]

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_twitter()
