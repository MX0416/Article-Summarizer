import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import ssl



def summarize():

    url = URLtext.get('1.0', 'end').strip() # strip() takes away useless characters such as new line
    # this try block desables SSL check
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download('punkt_tab')

    # url = 'https://www.cnn.com/2024/08/18/europe/zelensky-kursk-incursion-second-bridge-intl/index.html'

    article = Article(url)

    article.download()
    article.parse()
    # natural language processing
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    title.config(state='disable')
    author.config(state='disable')
    publication.config(state='disable')
    summary.config(state='disable')

    # print(f'Title: {article.title}')
    # print(f'Authors: {article.authors}')
    # print(f'Publication Date: {article.publish_date}')
    # print(f'Summary: {article.summary}')

    # analysis = TextBlob(article.text)
    # print(analysis.polarity)
    # print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')



# start of graphical user interface code
root = tk.Tk()
root.title("Article Summarizer")
root.geometry('1199x599')

# title
titleLabel = tk.Label(root, text="Title")
titleLabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg='#dddddd')
title.pack()

# author
authorLabel = tk.Label(root, text="Author")
authorLabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg='#dddddd')
author.pack()

# title
publicationLabel = tk.Label(root, text="Publication Date")
publicationLabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg='#dddddd')
publication.pack()

# summary
summaryLabel = tk.Label(root, text="Summary")
summaryLabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg='#dddddd')
summary.pack()

# URL
URLLabel = tk.Label(root, text="URL")
URLLabel.pack()

URLtext = tk.Text(root, height=1, width=140)
URLtext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)

btn.pack()




root.mainloop()