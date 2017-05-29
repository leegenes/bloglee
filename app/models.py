from app import db
from datetime import datetime
import mistune

class Post(db.Model):
    post_title = db.Column(db.Text)
    post_md = db.Column(db.Text)
    post_html = db.Column(db.Text)
    post_timestamp = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, primary_key=True,
                                unique=True)

    def __init__(self, post_id, content, title):
        self.post_id = id
        self.post_title = post_title
        self.post_md = self.get_md(content)
        self.post_html = self.get_html(self.md_content)
        self.post_timestamp = datetime.utcnow()

    def __repr__(self):
        return '<Title %r>' % (self.title)

    def get_md(self, content):
        with open(content, 'r') as f:
            md = f.read()
        return md

    def get_html(self, md_string):
        m = mistune.Markdown()
        return m(md_string)
