from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/gender", methods=["POST"])
def gender():

    gender = request.form.get("gender")

    return f"Siz tanlagan jins: {gender}"

app.run(debug=True)
