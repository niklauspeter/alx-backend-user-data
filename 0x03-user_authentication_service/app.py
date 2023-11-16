#!/usr/bin/env python3

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome() -> str:
    """ GET /
    Return:
        - welcome
    """
    return jsonify({"message": "Bienvenue"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
