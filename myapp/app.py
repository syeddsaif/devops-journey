from flask import Flask
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello — my DevOps project is live!"

@app.route("/status")
def status():
    now = datetime.datetime.now()
    disk = os.popen("df -h /").read()
    return f"""
    Server is up.
    Time: {now}
    Disk usage:
    {disk}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
