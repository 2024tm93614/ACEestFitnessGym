from flask import Flask, jsonify

app = Flask(__name__)

# Fake database
members = []

@app.route("/")
def home():
    return jsonify({
        "application": "ACEest Fitness & Gym API",
        "version": "1.3",
        "status": "running"
    })


@app.route("/init")
def init_database():
    global members
    members = []
    return jsonify({"message": "Database initialized"})


@app.route("/add")
def add_member():
    global members

    new_member = {
        "id": len(members) + 1,
        "name": f"Member{len(members)+1}",
        "plan": "Premium"
    }

    members.append(new_member)

    return jsonify({
        "message": "Member added successfully",
        "member": new_member
    })


@app.route("/members")
def get_members():
    return jsonify({
        "count": len(members),
        "members": members
    })

@app.route("/health")
def health_check():
    return jsonify({"status": "API is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)