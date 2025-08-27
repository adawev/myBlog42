import os
from flask import Flask, render_template, session, request

from article import Article

app = Flask(__name__)

@app.route('/set-session')
def set_session():
    session['user_id'] = 1
    return 'session set'

@app.route('/get-session')
def get_session():
    return f'user_id={session.get("user_id")}'

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
