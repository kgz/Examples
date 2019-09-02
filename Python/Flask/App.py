from flask import Flask
app = Flask(__name__, subdomain_matching=True)
app.config['SERVER_NAME'] = "localhost"


@app.route('/')
def hello():
    return "Hello World!"


@app.route("/", subdomain="app")
def olleh():
    return "Hello World!"[::-1]

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

