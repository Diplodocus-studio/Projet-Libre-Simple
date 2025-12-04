from flask import Flask, render_template, request, session, redirect, url_for
import pymongo
app = Flask(__name__)

mongo = pymongo.MongoClient("mongodb+srv://mateohiolle_db_user:<db_password>@post.qt7jab2.mongodb.net/?appName=Post")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)

#utiliser imgur pour image