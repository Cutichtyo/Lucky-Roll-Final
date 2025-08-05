from flask import Flask, render_template, jsonify
import random
import os

port = int(os.environ.get("PORT", 10000))
app = Flask(__name__)

# Danh sách phần thưởng
prizes = [
    {"name": "Voucher ăn uống", "type": "image", "url": "/static/images/voucher.jpg"},
    {"name": "Clip chúc mừng sinh nhật", "type": "video", "url": "/static/videos/birthday.mp4"},
    {"name": "Phần quà bí ẩn", "type": "image", "url": "/static/images/gift.jpg"},
    {"name": "Tiền bí ẩn", "type": "text", "amount": random.randint(10, 100)},
    {"name": "Thử thách Khủng long", "type": "game", "url": "/dino"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin')
def spin():
    prize = random.choice(prizes)
    if prize["type"] == "text":
        prize["amount"] = random.randint(10, 100)
    return jsonify(prize)

@app.route('/dino')
def dino_game():
    return render_template('dino.html')

@app.route('/flappy')
def flappy_game():
    return render_template('flappy.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
