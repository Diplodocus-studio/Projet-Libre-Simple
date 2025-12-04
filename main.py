from flask import Flask, render_template, request, session, redirect, url_for
import pymongo
app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://mateohiolle_db_user:ZLy9PpJT7ixl5hOM@post.qt7jab2.mongodb.net/?appName=Post")
db = client["SiteProjetLibre"]

app.secret_key = "ZLy9PpJT7ixl5hOM"

@app.route('/')
def index():

    user_post = list(db["posts"].find({"author": session['user']})) if 'user' in session else None

    popular_post = list(db["posts"].find({}))
    return render_template('index.html', user_post=user_post, popular_post=popular_post)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)

#utiliser imgur pour image