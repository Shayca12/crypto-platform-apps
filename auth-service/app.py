from flask import Flask, request, jsonify
import os
import hmac
import hashlib
import time

app = Flask(__name__)

SECRET = os.getenv("AUTH_SECRET", "dev-secret-change-me")
TOKEN_TTL_SECONDS = int(os.getenv("TOKEN_TTL_SECONDS", "3600"))

def sign(data: str) -> str:
    return hmac.new(SECRET.encode(), data.encode(), hashlib.sha256).hexdigest()

def make_token(username: str) -> str:
    # simple token: username:exp:signature
    exp = int(time.time()) + TOKEN_TTL_SECONDS
    payload = f"{username}:{exp}"
    sig = sign(payload)
    return f"{payload}:{sig}"

def verify_token(token: str) -> (bool, str):
    try:
        username, exp_str, sig = token.split(":")
        payload = f"{username}:{exp_str}"
        expected_sig = sign(payload)
        if not hmac.compare_digest(sig, expected_sig):
            return False, "bad_signature"
        if int(exp_str) < int(time.time()):
            return False, "expired"
        return True, "ok"
    except Exception:
        return False, "invalid_format"

@app.get("/healthz")
def healthz():
    return "ok,im fine", 200

@app.post("/auth/login")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    # demo auth only (in real life: DB + hashing + policies)
    if not username or not password:
        return jsonify({"error": "missing_username_or_password"}), 400

    token = make_token(username)
    return jsonify({"token": token})

@app.post("/auth/verify")
def verify():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify({"valid": False, "reason": "missing_bearer"}), 401

    token = auth.removeprefix("Bearer ").strip()
    ok, reason = verify_token(token)
    if not ok:
        return jsonify({"valid": False, "reason": reason}), 401

    return jsonify({"valid": True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

