import os

from slugify import slugify

class Article:
    def __init__(self, title):
        self.title = title
        self.content = ""
    @property
    def slug(self):
        return slugify(self.title)

    def load_content(self):
        with open(f"articles/{self.title}") as f:
            self.content = f.read()

    @classmethod
    def all(cls):
        titles = os.listdir("articles")
        slug_articles = {}
        for title in titles:
            slug = slugify(title)
            article = Article(title)
            article.load_content()
            slug_articles[slug] = article
        return slug_articles