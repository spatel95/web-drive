from flask import Flask, redirect, jsonify
from drive import DriveFiles
from config import Config

config = Config()

app = Flask(__name__)
files = DriveFiles.DriveFiles(config.DRIVE_DIR)


@app.route('/')
def empty():
    return redirect(config.REDIRECT_URL)


@app.route(config.REDIRECT_URL)
def main():
    # files.list_file("aa","/")
    response = jsonify([f.serialize() for f in files.list_file("aa","/")])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()
