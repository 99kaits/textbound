from flask import Flask, render_template, send_from_directory
from generate import gentext
app = Flask(__name__)

@app.route("/")
def web():
    return render_template('index.html', text=gentext())

if __name__ == "__main__":
    app.run(threaded=True)