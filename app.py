import os
from flask import Flask, render_template, session, request, make_response
import hashlib
from article import Article

app = Flask(__name__)

# @app.route('/set-session')
# def set_session():
#     session['user_id'] = 1
#     return 'session set'
#
# @app.route('/get-session')
# def get_session():
#     return f'user_id={session.get("user_id")}'

users={
    'admin' : '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
}
@app.route('/first-time')
def first_time():
    if 'seen' not in request.cookies:
        response = make_response('you are new here')
        response.set_cookie('seen', "1")
        return response

    seen = int(request.cookies['seen'])

    response = make_response(f'I have seen you {seen} times')
    response.set_cookie('seen', str(seen + 1))
    return response
@app.route('/')
def blog():
    articles = Article.all()
    return render_template('blog.html', articles=articles)

@app.route('/blog/<slug>')
def article(slug: str):
    articles = Article.all()
    article = articles[slug]
    return render_template('article.html', article=article)

@app.route('/admin')
def admin():
    return render_template('login.html')

@app.post('/admin')
def admin_login():
    username = request.form['username']
    password = request.form['password']

    if username not in users:
        return render_template('login.html', error='password/login xato')

    hashed = hashlib.sha256(password.encode()).hexdigest()
    return render_template('login.html', error='hali tayyor emas')
if __name__ == '__main__':
    app.run(port=4200, debug=True)
