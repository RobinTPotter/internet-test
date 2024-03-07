from flask import Flask
from pingtest import page as drops
from latencytest import page as lats

app = Flask(__name__)

@app.route("/")
@app.route("/drops")
def hello():
    return drops()

@app.route("/latency")
def hello2():
    return lats()

if __name__ == "__main__":
        app.run(debug=True)
