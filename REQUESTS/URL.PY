import requests

products = requests.get('https://dummyjson.com/products')


product_Json = products.json()

#print(type(product_Json['products']))

for product_dict in product_Json['products']:
    for key, value in product_dict.items():
        print('{:>5}:{}'.format(key,value))