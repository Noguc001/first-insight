import feedparser
import requests

def fetch_feed(url):
    insights_feed = requests.get(url)
    return feedparser.parse(insights_feed.text)

def format_post(post):
    return ("Title: " + post['title'] + "\n \n" +
    "Summary:\n" +
    post['summary'])
