#!/usr/bin/env python3

from flask import Flask, escape, request, jsonify, send_from_directory
from flask_sslify import SSLify

import offset


app = Flask(__name__)
# sslify = SSLify(app)


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/')
def hello():
    name = request.args.get("name", "World")
    return jsonify({'offset': offset.offset("America/Los_Angeles")})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
