from flask import Flask
from flask import render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


@app.route("/")
def get_the_website():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(threaded=True ,port=5000)
