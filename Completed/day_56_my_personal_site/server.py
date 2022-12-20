from flask import *

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


app.run("127.0.0.1", 5000, debug=True)
