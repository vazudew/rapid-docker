from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

@app.route("/health")
def info():
    return "health is ok!\n"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/fetch")
def fetch_product():
    return "fetch is ok!\n"

@app.route("/import")
def import_data():
    return "import is ok!\n"

@app.route("/recommend")
def recommend_prodcut():
    return "recommend is ok!\n"

def printHello():
    print("Hello World!")

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
