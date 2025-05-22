from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

connection_string = "mongodb+srv://mariaancabalutoiu:jeyuauQzrxWpIDim@cluster0.e83xcgo.mongodb.net/"
client = MongoClient(connection_string)
db = client["gettingStarted"]

@app.route("/login")
def login():
    user = request.args.get("user")
    password = request.args.get("password")
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{password}'"
    db.execute(query)

@app.route("/comment")
def comment():
    comment = request.args.get("text")
    return f"User said: {comment}"

if __name__ == "__main__":
    app.run(debug=True)