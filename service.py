#!/usr/bin/env python3

from flask import Flask, escape, request, jsonify

import offset


app = Flask(__name__)

@app.route('/')
def index():
	return ""


@app.route('/api/')
def hello():
    name = request.args.get("name", "World")
    return jsonify({'offset': offset.offset("America/Los_Angeles")})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
