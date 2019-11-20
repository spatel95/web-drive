from flask import Flask, redirect
from drive import DriveFiles
app = Flask(__name__)
files = DriveFiles.DriveFiles("/tmp")


@app.route('/')
def empty():
    return redirect("/drive")


@app.route('/drive')
def main():
    return files.list_file("aa","/")


if __name__ == '__main__':
    app.run()
