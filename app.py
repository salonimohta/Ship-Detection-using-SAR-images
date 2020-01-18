from flask import Flask, render_template, request
import os
app = Flask(__name__)


@app.route("/")
def frontPage():

    return render_template('frontPage.html')


@app.route("/karachi")
def karachi():
    os.system('python csv2json.py karachi')
    return render_template('markPoints.html')


@app.route("/kandla")
def kandla():
    os.system('python csv2json.py kandla')
    return render_template('markPoints.html')


if __name__ == "__main__":
    app.run(debug=True)
