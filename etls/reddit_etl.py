import sys
import praw
from praw import Reddit

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
        print("connectd to reddit")
        return reddit
    except Exception as e:
        print(s)
        sys.exit(1)