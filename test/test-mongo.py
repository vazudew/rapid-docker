from pymongo import MongoClient

user='admin'
password='pass'
hostname='localhost'
port='27017'
MONGODB_URI=f"mongodb//{user}:{password}@{hostname}:{port}/"
print(f"URL : {MONGODB_URI}")

client = MongoClient('mongodb://admin:pass@localhost:27017/')

try:
    info = client.server_info() # Forces a call.
    print(f"inf: {info}")
except ServerSelectionTimeoutError:
    print("server is down.")

if __name__ == '__main__':
    database = client['mini_test']
    collection= database['products']
    products = collection.find()
    print("HERE!")
    for product in products:
        print(f"product : {product}")