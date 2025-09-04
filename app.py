from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Trade Haven is live! v2"  # <— plain text
@app.route("/privacy-policy")
def privacy():
    return """
    <h1>Privacy Policy</h1>
    <p>This is the Trade Haven Privacy Policy page.</p>
    <p>We respect your privacy. Full details coming soon.</p>
    """
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
