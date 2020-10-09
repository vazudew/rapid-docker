import json
import random

hexaDigitSet = set()

category_product_price_map = {
        'electronics' : [
                            {'laptop' :900}, 
                            {'pc': 550}, 
                            {'camera' : 255 }, 
                            {'smartphone': 200 }, 
                            {'mouse' : 25 }
                        ],
        'furniture' :   [ 
                            {'sofa' : 300}, 
                            {'bed' :400}, 
                            {'chair' : 50}, 
                            {'table': 110}
                        ],
        'cosmetics' :   [
                            {'lipstick' :20 }, 
                            {'perfume': 55}, 
                            {'cream' :20}
                        ],
        'books' :       [
                            {'novel' : 35}, 
                            {'poem' : 20}, 
                            {'magazine': 10}
                        ],
        'software' :    [
                            {'game': 10}, 
                            {'anti-virus': 50}
                        ]
}

vendors = [
            'Amazon ag', 'Bella GmbH', 'President ag', 
            'Europa Ag', 'P-tech', 'Agility', 'Spinsoft',
            'Bavarian Shop', 'Ayurveda', 'Agenda', 'Chanel'
        ]

def randomVendorDetail():
    priceFactor = random.randint(50, 130)/100
    rating = random.randint(1,5)
    return priceFactor, rating

def get25HexaDigit():
    hexaNumber = "%025x" % random.randrange(16**25)

    #find unique hexanumber
    while hexaNumber in hexaDigitSet:
        hexaNumber = "%025x" % random.randrange(16**25)
    hexaDigitSet.add(hexaNumber)
    
    return hexaNumber

def prepareRandomizedData(nRow):
    datasetList = []
    for i in range(nRow):
        category, productList= random.choice(list(category_product_price_map.items()))
        product, price=random.choice(list(productList[0].items()))
        pf, rating = randomVendorDetail()
        datasetList.append (
                {"_id":
                    {
                        "$oid": get25HexaDigit()
                    },
                    'product' : product,
                    'category' : category,
                    'vendor': random.choice(vendors),
                    'price' : "%.2f" % (price * pf),
                    'rating' : rating
                }
        )
    return datasetList

if __name__ == '__main__':
    print('hello')
    number_of_items = random.randint(120, 175)
    print(f'#No of Items {number_of_items}')
    dataset = prepareRandomizedData(number_of_items)

    for m in dataset:
        print(m)
        print('-----')

    with open('product.json', 'w') as json_file:
        json.dump(dataset, json_file)

