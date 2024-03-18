# NFL Twitter and Web Scraper

This Python script fetches tweets related to NFL Free Agency and NFL Draft using the Twitter API and scrapes news articles from the web using Beautiful Soup.

## Prerequisites
- Python 3.x
- Tweepy library
- BeautifulSoup library

## Installation

1. Clone the repository.
  
2. Install the required dependencies:
    ```bash
    pip install tweepy beautifulsoup4
    ```

## Usage

1. Replace `'YOUR_CONSUMER_KEY'`, `'YOUR_CONSUMER_SECRET'`, `'YOUR_ACCESS_TOKEN'`, and `'YOUR_ACCESS_TOKEN_SECRET'` in the script with your own Twitter API credentials.
2. Replace `'https://www.example.com'` in the script with the actual URL of the website you want to scrape news from.
3. Run the script:
    ```bash
    python nfl_scraper.py
    ```

## Output
- The script will print tweets related to NFL Free Agency and NFL Draft.
- It will also display news articles related to NFL Free Agency and NFL Draft along with their titles and links.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
