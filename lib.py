import feedparser
import requests

def fetch_feed(url):
    """
    Get rss feed data from the url
    """
    insights_feed = requests.get(url)
    return feedparser.parse(insights_feed.text)


def format_post(post):
    """
    Display a post
    """
    return ("Title: " + post['title'] + "\n \n" +
    "Summary:\n" +
    post['summary'])
