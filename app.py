Step 2: Update app.py to serve static file

Now add this to your app.py:

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/privacy-policy")
def privacy():
    return render_template("privacy-policy.html")

# ✅ THIS is the key fix for validation
@app.route("/validation-key.txt")
def serve_validation_key():
    return send_from_directory(os.getcwd(), "validation-key.txt", mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
