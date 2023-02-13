import json
emp = '''{"id":101,"name": "joshi","sal":40000}'''
emp_dict = {"id":102,"name":"gowd", "sal":50000}
#convert the json string to python dict
emp_dict1 = json.loads(emp)
print(emp_dict1)