import requests

products = requests.get('https://dummyjson.com/products')

#print(products)
#print(type(products))

product_Json = products.json()
#print(type(product_Json))
print(type(product_Json['products']))

for product_dict in product_Json['products']:
    print(product_dict)
