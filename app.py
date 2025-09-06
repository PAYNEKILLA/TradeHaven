from flask import Flask, render_template, send_from_directory, request, jsonify
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
    return send_from_directory(os.getcwd(), "validation-key.txt", mimetype="text/plain")

# ✅ NEW: Pi Payment Approval Endpoint
@app.route("/approve-payment", methods=["POST"])
def approve_payment():
    data = request.get_json()
    payment_id = data.get("paymentId")
    print(f"Approving payment: {payment_id}")
    return jsonify({ "success": True })

# ✅ NEW: Pi Payment Completion Endpoint
@app.route("/complete-payment", methods=["POST"])
def complete_payment():
    data = request.get_json()
    payment_id = data.get("paymentId")
    txid = data.get("txid")
    print(f"Completing payment: {payment_id} with txid: {txid}")
    return jsonify({ "success": True })

