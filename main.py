import feedparser
import requests

BOT_TOKEN = "BURAYA_TOKEN"
CHAT_ID = "BURAYA_CHAT_ID"

RSS_URL = "https://news.google.com/rss/search?q=israel+iran+war+OR+attack+OR+missile"

KEYWORDS = ["israel", "iran", "attack", "war", "missile", "strike"]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

feed = feedparser.parse(RSS_URL)

for entry in feed.entries:
    title = entry.title.lower()

    if any(k in title for k in KEYWORDS):
        send_telegram("🚨 BREAKING NEWS\n\n" + entry.title + "\n\n" + entry.link)
        break
