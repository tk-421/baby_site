import os

from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()
