import json

data = [{'b': 2}, {'c': 3}, {'d': 4}]
json1 = json.dumps(data)
print(json1)

data = [{'b': 2}, {'c': 3}, {'d': 4}]
json2 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
print(json2)

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(jsonData)
print(text)

