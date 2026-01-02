from flask import Flask, jsonify, send_from_directory
import threading
import time

app = Flask(__name__, static_folder="static")

jump_state = False

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/jump")
def jump():
    return jsonify({"jump": jump_state})

@app.route("/trigger", methods=["POST"])
def trigger():
    global jump_state

    if not jump_state:
        jump_state = True

        def reset_jump():
            global jump_state
            time.sleep(14)
            jump_state = False

        threading.Thread(target=reset_jump).start()

    return jsonify({"status": "ok", "jump": jump_state})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
