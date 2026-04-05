from flask import Flask, jsonify
from flask_cors import CORS   # 👈 ADD THIS

app = Flask(__name__)
CORS(app)   # 👈 ADD THIS

count = 0

@app.route('/increase')
def increase():
    global count
    count += 1
    return jsonify(count=count)

@app.route('/decrease')
def decrease():
    global count
    count -= 1
    return jsonify(count=count)

app.run(debug=True)