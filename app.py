from flask import Flask, jsonify
from gym_logic import init_db, add_member, get_members

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "ACEest Fitness DevOps API Running"
    })


@app.route("/init")
def initialize_database():
    init_db()
    return jsonify({"status": "database initialized"})


@app.route("/add")
def add_sample_member():
    add_member("Rahul", 25, "Premium")
    return jsonify({"status": "sample member added"})


@app.route("/members")
def members():

    data = get_members()

    result = []

    for m in data:
        result.append({
            "name": m[0],
            "age": m[1],
            "plan": m[2]
        })

    return jsonify(result)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)