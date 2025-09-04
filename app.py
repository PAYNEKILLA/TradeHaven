from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Trade Haven is live! v2"  # <— plain text
@app.route("/privacy-policy")
def privacy():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Privacy Policy - Trade Haven</title>
  <style>
    :root{--pi:#6C63FF;--ink:#222;--muted:#555;--bg:#fafafa;}
    html,body{background:var(--bg);margin:0;padding:0;}
    .wrap{max-width:840px;margin:48px auto;padding:0 20px;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:var(--ink);line-height:1.6}
    h1{color:var(--pi);margin:0 0 12px}
    h2{margin:32px 0 8px}
    p,li{color:var(--muted)}
    .card{background:#fff;border-radius:14px;box-shadow:0 6px 24px rgba(0,0,0,.06);padding:28px}
    .meta{font-size:14px;margin-bottom:18px;color:#777}
    a{color:var(--pi);text-decoration:none}
    a:hover{text-decoration:underline}
    .footer{margin-top:28px;font-size:13px;color:#777}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <div class="meta">Trade Haven • Pi Network Testnet</div>
      <h1>Privacy Policy</h1>
      <p>Welcome to <strong>Trade Haven</strong>. We respect your privacy and are committed to protecting your information.</p>

      <h2>What We Collect</h2>
      <ul>
        <li>Basic app analytics (errors, uptime) to improve reliability.</li>
        <li>Pi user data only when you explicitly grant permission via Pi Browser.</li>
      </ul>

      <h2>How We Use Data</h2>
      <ul>
        <li>To operate core features of the app.</li>
        <li>To keep the service secure and performant.</li>
      </ul>

      <h2>What We Don’t Do</h2>
      <ul>
        <li>No selling of personal data.</li>
        <li>No sharing with third parties without your consent.</li>
      </ul>

      <h2>Security</h2>
      <p>Transactions and permissions in Pi Browser are handled using Pi’s secure, permission-based flows.</p>

      <h2>Contact</h2>
      <p>Questions? Reach us at: <a href="mailto:support@tradehaven.app">support@tradehaven.app</a></p>

      <div class="footer">Last updated: Sept 2025 • This is an initial policy for testing and verification.</div>
    </div>
  </div>
</body>
</html>
    """
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
