from flask import render_template, Markup
from app import app, models
from datetime import datetime

@app.route('/')
# def home():
#      return render_template('home.html',
#                             title='Home')

@app.route('/blog')
def blog():
    q = models.Post.query.all()
    posts = []
    for p in q:
        posts.append({
            'post_title': p.post_title,
            'post_timestamp': p.post_timestamp,
            'post_id': p.post_id})
    return render_template('blog/blog_directory.html',
                            title='Blog',
                            posts=posts)

@app.route('/blog/<int:post_id>')
def post(post_id):
    p = models.Post.query.filter_by(post_id=post_id).first()
    post = {'post_id': p.post_id,
            'post_html': Markup(p.post_html),
            'post_timestamp': p.post_timestamp,
            'post_title': p.post_title}
    return render_template('blog/post.html',
                            title='Blog {}'.format(post_id),
                            post=post)

@app.route('/soon.gif')
def coming_soon():
    return render_template('coming_soon.html',
                            title='OH NO!')
