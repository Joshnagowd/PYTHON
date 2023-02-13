import json
emp_dict = {'id': 111,'name':'ram', 'sal':50000}
emp_json = json.dumps(emp_dict)
print(emp_json)
f = open("ram.json",'w')
json.dump(emp_dict,f)
f.close()
'''write open("krish.json",'w') as f:
    json.dump(emp_dict.f)'''