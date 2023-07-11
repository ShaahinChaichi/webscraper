from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tags = soup.find_all(name="a", rel="noreferrer")
article_texts = []
article_link = []

for article in article_tags:
    article_texts.append(article.getText())
    article_link.append(article.getLink())

article_upvotes = soup.find_all(name="span", class_="score")

print(article_texts)
print(article_link)
print(article_upvotes)

