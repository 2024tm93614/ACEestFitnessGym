from flask import Flask, jsonify

app = Flask(__name__)

# Fake database
members = []

@app.route("/")
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym API"})


@app.route("/init")
def init_database():
    global members
    members = []
    return jsonify({"message": "Database initialized"})


@app.route("/add")
def add_member():
    global members
    new_member = {"name": "Rahul", "plan": "Premium"}
    members.append(new_member)
    return jsonify({"message": "Member added", "member": new_member})


@app.route("/members")
def get_members():
    return jsonify(members)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)