from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    """Home page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)