from flask import Flask, redirect, url_for, render_template, request, flash
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

def printHello():
    print("Hello World!")

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
