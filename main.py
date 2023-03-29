from flask import Flask, render_template, request
import pymysql
import pymysql.cursors 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html.jinja")

@app.route("/feed")
def post_feed():
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM `posts` ORDER BY `timestamp`")

    results = cursor.fetchall()

    return  render_template("feed.html.jinja",
  posts=results
  )

@app.route("/sign-in")
def sign_in():
    return render_template("sign_in.html.jinja")

@app.route("/sign-up")
def sign_up():
    if request.method == "POST":
       cursor = connection.cursor()

       cursor.execute("""
       INSERT INTO `users`(`username`, `email`, `display_name`,`password`,`bio`,`photo`)
       VALUES (%s, %s, %s, %s, %s, %s)
       """, [])
       
       return request.form
    elif request.method== "GET":
       return render_template("sign_up.html.jinja")


connection = pymysql.connect(
    host="10.100.33.60",
    user="mwilliams",
    password="220467419",
    database="mwilliams_socialmedia",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)


if __name__ =="__main__": 
    app.run(debug=True)