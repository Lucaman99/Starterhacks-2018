import json
import time
import glob
import os
from shutil import copyfile
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from IPython import embed
import logging


app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
app.logger.addHandler(stream_handler)


@app.route("/")
def main():
	return render_template('dashboard.html')

@app.route("/healthhistory", methods=['POST', 'GET'])
def main():
	print("reached!")


@app.route("/healthtraking", methods=['POST', 'GET'])
def main():
	return render_template('')

if __name__ == "__main__":
    app.run(debug = True, port=3000)