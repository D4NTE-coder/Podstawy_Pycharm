from flask import Flask, render_template, redirect, session, url_for
import config
import auth
import recommendation

app = Flask(__name__)
app.secret_key = config.Config.SECRET_KEY

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
    if data is None:
        return render_template("error.html", message="Błąd podczas pobierania rekomendacji")
    return render_template("concerts.html", data=data)

@app.route("/logout")
def logout_user():
    return auth.logout()

if __name__ == "__main__":
    app.run(debug=True)