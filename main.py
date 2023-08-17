from flask import Flask
from flask import render_template
import os
# from werkzeug.middleware.proxy_fix import ProxyFix

# app = Flask(__name__)
#
# # app.wsgi_app = ProxyFix(
# #     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# # )
#
# print("Starting main app on 8080...")
#
# @app.route("/")
# def get_the_website():
#     return render_template("index.html")
#
#
# print("Before start")
# port = int(os.getenv('PORT', 8080))
# print('Listening on port %s' % port)
#
# # if __name__ == "__main__":
# #     app.run(threaded=True, port=8080)
#
# app.run(port=port, debug=True)


import os
import http.server
import socketserver

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Python is running on Qoddi! You requested %s' % (self.path)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 8080))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()