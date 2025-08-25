import os
from slugify import slugify
from flask import Flask, render_template, abort

from article import Article

app = Flask(__name__)


@app.route('/')
def blog():
    articles = Article.all()
    return render_template('blog.html', articles=articles)

@app.route('/blog/<slug>')
def article(slug: str):
    articles = Article.all()
    article = articles[slug]
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run(port=4200, debug=True)
