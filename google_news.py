import requests
from bs4 import BeautifulSoup

def get_google_news_headlines():
    url = "https://news.google.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headlines = []
    for headline in soup.find_all('h3', class_='ipQwMb ekueJc RD0gLb'):
        headlines.append(headline.text)
    
    return headlines

if __name__ == "__main__":
    top_headlines = get_google_news_headlines()
    print("Top Stories from Google News:")
    for idx, headline in enumerate(top_headlines, start=1):
        print(f"{idx}. {headline}")
