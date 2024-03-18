import tweepy
from bs4 import BeautifulSoup
import requests

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate to Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Search terms for NFL Free Agency and NFL Draft
search_terms = ['NFL Free Agency', 'NFL Draft']

# Function to fetch tweets
def fetch_tweets(query):
    tweets = api.search(q=query, lang='en', count=10)
    return tweets

# Function to scrape news related to NFL Free Agency and NFL Draft
def scrape_news():
    news_articles = []
    for term in search_terms:
        url = f'https://www.example.com/search?q={term.replace(" ", "+")}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            title = article.find('h2').get_text()
            link = article.find('a')['href']
            news_articles.append({'title': title, 'link': link})
    return news_articles

# Fetch tweets
for term in search_terms:
    tweets = fetch_tweets(term)
    print(f"Tweets related to '{term}':")
    for tweet in tweets:
        print(f"- {tweet.text}")

# Scrape news
news = scrape_news()
print("\nNews articles related to NFL Free Agency and NFL Draft:")
for article in news:
    print(f"- {article['title']}: {article['link']}")
