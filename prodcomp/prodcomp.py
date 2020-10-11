from flask import Flask, redirect, url_for, render_template, request, flash
import logging

from pymongo import MongoClient
import random 

logging.basicConfig(
     filename='prodcomp_logger.log',
     level=logging.DEBUG, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )

user='admin'
password='pass'
hostname='mongodb'
port='27017'
MONGODB_URI=f'mongodb://{user}:{password}@{hostname}:{port}/'
logging.debug(f"URL : {MONGODB_URI}")
MACHINE_ID=("%05x" % random.randrange(16**5)).upper()
logging.debug(f"ID : {MACHINE_ID}")

#Try one of these !
#client = MongoClient('mongodb://admin:pass@mongodb:27017/')
client = MongoClient(MONGODB_URI)

database = client['mini_test']
collection= database['products']

app = Flask(__name__)


def initDB():
    #pass
    try:
        info = client.server_info() # Forces a call.
        logging.debug(f"inf: {info}")
        print(f"inf: {info}")
    except ServerSelectionTimeoutError:
        logging.debug(f"inf: server is down")
        print("server is down.")

@app.route("/health")
def info():
    return "health is ok!\n"

@app.route("/")
def index():
    initDB()
    info = {
        "MongoDB URL" : f"{hostname}:{port}",
        "MongoDB Express URL": f"localhost:8985",
        "ME Username": "admin",
        "ME Password" : "pass"
    }
    return render_template('index.html', id=MACHINE_ID, message="ProdComp Service  welcomes!", information = info)

@app.route("/fetch", methods=['GET'])
def fetch_product():
    products = collection.find()
    productsList=[]
    for product in products:
        productsList.append(product)
        logging.debug(f"product: {product}")
        print(f"product:{product}")
    return render_template('list_products.html', id=MACHINE_ID, message="Product list",  productsList=productsList)

@app.route("/import", methods=['GET'])
def import_data():
    logging.debug(f"import file called")
    return  render_template('upload.html',  id=MACHINE_ID)

@app.route("/upload", methods=['POST'])
def upload():
    logging.debug(f"{request} and {request.headers['Content-Type']}")
    logging.debug(f"iupload called {request.data}")
    if request.method == "POST":
        logging.debug(f"POST METHOD")
        if request.files:
            logging.debug(f"files inside")
            logging.debug(f"request files : {request.files}")
            importFile = request.files["importJsonFile"]
            with open(importFile) as json_file:
                data = json.load(json_file)
                logging.debug(f"DATA :{data}")
    return  "upload item"


@app.route("/recommend")
def recommend_prodcut():
    return "recommend is ok!\n"

def printHello():
    print("Hello World!")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
