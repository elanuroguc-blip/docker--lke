from flask import Flask, jsonify, request

app = Flask(__name__)

# 🔥 STATE (sunucu hafızası)
last_country = None

@app.route("/select-country", methods=["POST"])
def select_country():
    global last_country
    data = request.json
    last_country = data.get("country")
    return jsonify({
        "message": "Ülke kaydedildi",
        "country": last_country
    })

@app.route("/last-country")
def get_last_country():
    return jsonify({
        "last_country": last_country
    })

app.run(host="0.0.0.0", port=5000)
