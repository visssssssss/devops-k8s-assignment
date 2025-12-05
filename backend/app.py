from flask import Flask
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/api")
def api():
    return {"message": "Hello from backend"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
