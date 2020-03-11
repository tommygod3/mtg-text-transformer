import json, csv
import tqdm
import praw

def get_valid_title(submission):
    if "[" not in submission.title and "|" not in submission.title:
        return submission.title.strip().replace("\n", " ")

def get_highest_valid_comment(submission):
    for comment in list(submission.comments):
        if "[" not in comment.body and "|" not in comment.body:
            return comment.body.strip().replace("\n", " ")


with open("reddit-secret.json") as reader:
    secret = json.load(reader)

reddit = praw.Reddit(client_id=secret["client_id"],
                     client_secret=secret["client_secret"],
                     user_agent="mtg-text-transformer by /u/tommygod3 https://github.com/tommygod3/mtg-text-transformer")

subreddit = reddit.subreddit("magicTCG")

maximum_posts = 900

with open("mtg_data.csv", "w") as writer:
    csv_writer = csv.writer(writer, delimiter="|")
    csv_writer.writerow(["Title", "Comment"])
    for submission in tqdm.tqdm(subreddit.hot(limit=maximum_posts), total=maximum_posts):
        title = get_valid_title(submission)
        top_comment = get_highest_valid_comment(submission)
        if not title is None and not top_comment is None:
            csv_writer.writerow([title, top_comment])
