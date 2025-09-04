from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")  # ✅ serve your real HTML file

@app.route("/privacy-policy")
def privacy():
    return render_template("privacy-policy.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
