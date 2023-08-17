from flask import Flask
from flask import render_template
import os
# from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# app.wsgi_app = ProxyFix(
#     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# )

print("Starting main app on 8080...")

@app.route("/")
def get_the_website():
    return render_template("index.html")


print("Before start")
port = int(os.getenv('PORT', 8080))
print('Listening on port %s' % (port))

# if __name__ == "__main__":
#     app.run(threaded=True, port=8080)

app.run(port=port)
