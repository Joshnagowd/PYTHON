#json string to python dict
import json
emp = '''{"id":101,"name": "joshi","sal":40000}'''
emp_dict = json.loads(emp)
print(emp_dict)
print(type(emp_dict))
for key, value in emp_dict.items():
    print('{}:{}'.format(key,value))