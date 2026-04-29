from flask import Flask, jsonify

app = Flask(__name__)

# Fake database
members = []

@app.route("/")
def home():
    return {
        "message": "Use /v1 or /v2 for A/B testing"
    }


@app.route("/v1")
def old_version():
    return {
        "version": "v1 (A/B TEST - OLD)",
        "message": "This is old version"
    }

@app.route("/v2")
def new_version():
    return {
        "version": "v2 (A/B TEST - NEW)",
        "message": "This is new version"
    }

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
    if not members:
        return jsonify({"message": "No members found"})

    return jsonify({
        "total_members": len(members),
        "members": members
    })

@app.route("/delete/<int:member_id>")
def delete_member(member_id):
    global members

    members = [m for m in members if m["id"] != member_id]

    return jsonify({
        "message": f"Member {member_id} deleted"
    })

@app.route("/health")
def health_check():
    return jsonify({"status": "API is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)