import json
import praw

with open("reddit-secret.json") as reader:
    secret = json.load(reader)

reddit = praw.Reddit(client_id=secret["client_id"],
                     client_secret=secret["client_secret"],
                     user_agent="mtg-text-transformer by /u/tommygod3 https://github.com/tommygod3/mtg-text-transformer")

subreddit = reddit.subreddit("magicTCG")

for submission in subreddit.hot(limit=10):
    print(f"Title: {submission.title}")
    print(f"Comment: {submission.comments[0].body}")

