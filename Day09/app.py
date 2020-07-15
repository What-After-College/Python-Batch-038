from flask import Flask
app = Flask(__name__)

@app.route("/")
def func():
    return "Hello World"

@app.route("/thor")
def f():
    return "Hello thor"

@app.route("/<name>")
def greetings(name):
    return "Hello " + name

if __name__ == "__main__":
    app.run(debug=True, port=8000)