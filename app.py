from flask import Flask, render_template, send_from_directory, request, jsonify
import os, requests

app = Flask(__name__)

# === ROUTES YOU ALREADY HAVE ===

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/privacy-policy")
def privacy():
    return render_template("privacy-policy.html")

@app.route("/validation-key.txt")
def validation_key():
    return send_from_directory(os.getcwd(), "validation-key.txt", mimetype="text/plain")


# === ADD THESE PAYMENT ROUTES ===

PI_API_KEY = os.environ.get("PI_API_KEY")
PI_API_BASE = "https://api.minepi.com"

def pi_headers():
    return {
        "Authorization": f"Key {PI_API_KEY}",
        "Content-Type": "application/json"
    }

@app.route("/create_payment", methods=["POST"])
def create_payment():
    data = request.get_json(force=True) or {}
    amount = float(data.get("amount", 0))
    memo = (data.get("memo") or "Trade Haven Payment")[:64]
    metadata = data.get("metadata") or {}

    try:
        r = requests.post(
            f"{PI_API_BASE}/v2/payments",
            headers=pi_headers(),
            json={
                "amount": amount,
                "memo": memo,
                "metadata": metadata
            },
            timeout=10
        )
        return (r.text, r.status_code, {"Content-Type": "application/json"})
    except Exception as e:
        app.logger.exception("create_payment failed")
        return jsonify({"error": str(e)}), 500

@app.route("/approve_payment", methods=["POST"])
def approve_payment():
    data = request.get_json(force=True) or {}
    payment_id = data.get("paymentId")
    if not payment_id:
        return jsonify({"error": "paymentId missing"}), 400

    try:
        r = requests.post(
            f"{PI_API_BASE}/v2/payments/{payment_id}/approve",
            headers=pi_headers(),
            json={},
            timeout=10
        )
        return (r.text, r.status_code, {"Content-Type": "application/json"})
    except Exception as e:
        app.logger.exception("approve_payment failed")
        return jsonify({"error": str(e)}), 500

@app.route("/complete_payment", methods=["POST"])
def complete_payment():
    data = request.get_json(force=True) or {}
    payment_id = data.get("paymentId")
    txid = data.get("txid")  # optional
    if not payment_id:
        return jsonify({"error": "paymentId missing"}), 400

    try:
        r = requests.post(
            f"{PI_API_BASE}/v2/payments/{payment_id}/complete",
            headers=pi_headers(),
            json={"txid": txid} if txid else {},
            timeout=10
        )
        return (r.text, r.status_code, {"Content-Type": "application/json"})
    except Exception as e:
        app.logger.exception("complete_payment failed")
        return jsonify({"error": str(e)}), 500
