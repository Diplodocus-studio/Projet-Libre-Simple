from flask import Flask, render_template, request, session, redirect, url_for
import pymongo
app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://mateohiolle_db_user:ZLy9PpJT7ixl5hOM@post.qt7jab2.mongodb.net/?appName=Post")
db = client["SiteProjetLibre"]

app.secret_key = "ZLy9PpJT7ixl5hOM"

@app.route('/')
def index():

    user_post = list(db["posts"].find({"author": session['user']})) if 'user' in session else None

    trending_post = list(db["posts"].find({}))
    return render_template('index.html', user_post=user_post, trending_post=trending_post)


@app.route("/signin", methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        db_users = db['users']
        user = db_users.find_one({'user_id' : request.form['user_id']})
        if user:
            if request.form["password"] == user["user_password"]:
                session['user'] = request.form['user_id']
                return redirect(url_for('index'))
            else:
                return render_template('signin.html', error="Incorrect password")
        else:
            return render_template('signin.html', error="Incorrect username")
    else:
        return render_template('signin.html')
    

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        db_users = db['users']
        new_user = db_users.find_one({'user_id' : request.form['user_id']})

        if new_user : 
            return render_template('signup.html', error="Username already used")
        else:
            if request.form['password'] == "" or request.form['user_id'] == "" or request.form['confirm_password'] == "":
                return render_template('signup.html', error="Empty field")
            else:
                if request.form['password'] == request.form['confirm_password']:
                    db_users.insert_one({
                        'user_id' : request.form['user_id'],
                        'user_password' : request.form['password']
                    })
                    session['user'] = request.form['user_id']
                    return redirect(url_for('index'))
                else:
                    return render_template('signup.html', error="Passwords not match")
    else:
        return render_template('signup.html')


@app.route('/signout')
def signout():
    session.clear()
    return redirect(url_for("index"))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()

    if query == '':
        results = list(db['posts'].find({}))
    else:
        results = list(db['posts'].find({
            "$or" : [
                {"title" : {"$regex" : query, "$options" : "i"}},
                {"content" : {"$regex" : query, "$options" : "i"}},
                {"author" : {"$regex" : query, "$options" : "i"}}
            ]
        }))

    return render_template("search_results.html", posts = results, query = query)

@app.route('/post')
def post():
    #media =
    return redirect(url_for("post.html"))

@app.route("/publish", methods=['POST', 'GET'])
def publish():
    if 'user' not in session:
        return render_template('login.html')
    
    if request.method == 'POST':
        db_posts = db['posts']
        title = request.form['title']
        media = request.form['media']
        content = request.form['content']
        author = session['user']

        if title and content and media:
            db_posts.insert_one({
                'title' : title,
                'media' : media,
                'content' : content,
                'author' : author
            })
            return redirect(url_for('index'))
        else:
            return render_template('publish.html', erreur="Please Fill All Fields")
    else:
        return render_template('publish.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)

#utiliser imgur pour image