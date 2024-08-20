import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import ssl

# this try block desables SSL check
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt_tab')

url = 'https://www.cnn.com/2024/08/18/europe/zelensky-kursk-incursion-second-bridge-intl/index.html'

article = Article(url)

article.download()
article.parse()
# natural language processing
article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')



analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

# start of graphical user interface code

changes