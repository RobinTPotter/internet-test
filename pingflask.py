from flask import Flask
from pingtest import page

app = Flask(__name__)

@app.route("/")
def hello():
    return page()
    
if __name__ == "__main__":
        app.run(debug=True)