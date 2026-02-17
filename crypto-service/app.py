from datetime import datetime
from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

AUTH_VERIFY_URL = os.getenv("AUTH_VERIFY_URL", "http://auth-service:5000/auth/verify")
COINGECKO_BASE_URL = os.getenv("COINGECKO_BASE_URL", "https://api.coingecko.com/api/v3")
REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "5"))

@app.get("/healthz")
def healthz():
    return "ok", 200

def verify_with_auth_service(auth_header: str) -> bool:
    r = requests.post(
        AUTH_VERIFY_URL,
        headers={"Authorization": auth_header},
        timeout=REQUEST_TIMEOUT
    )
    return r.status_code == 200

@app.get("/crypto/price")
def price():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return jsonify({"error": "missing_bearer"}), 401

    if not verify_with_auth_service(auth_header):
        return jsonify({"error": "invalid_token"}), 401

    coin = request.args.get("coin", "bitcoin")
    vs = request.args.get("vs", "usd")

    url = f"{COINGECKO_BASE_URL}/simple/price"
    params = {"ids": coin, "vs_currencies": vs}

    r = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
    r.raise_for_status()
    data = r.json()

    if coin not in data or vs not in data[coin]:
        return jsonify({"error": "unexpected_response", "raw": data}), 502

    return jsonify({
    "coin": coin,
    "vs": vs,
    "price": data[coin][vs],
    "source": "coingecko",
    "fetched_at": datetime.utcnow().isoformat() + "Z"
})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

