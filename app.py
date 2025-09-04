
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/privacy-policy")
def privacy():
    return render_template("privacy-policy.html")

@app.route("/validation-key.txt")
def validation_key():
    # serves validation-key.txt from the repo root
    return send_from_directory(os.getcwd(), "validation-key.txt", mimetype="text/plain")
