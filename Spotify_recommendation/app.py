from flask import Flask, render_template, redirect, session, url_for
import config
import auth
import recommendation
from auth import logout

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return auth.login()

@app.route("/callback")
def callback():
    return auth.callback()

@app.route("/recommend")
def recommend():
    data = recommendation.get_recommendations()
    return render_template("recommendations.html", data=data) # Wysyłamy dane do HTML

@app.route('/logout')
def logout_user():
    return auth.logout()

if __name__ == "__main__":
    app.run(debug=True,)