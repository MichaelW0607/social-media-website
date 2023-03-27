from flask import Flask, render_template
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