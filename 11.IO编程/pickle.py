import json
d = dict(name='XXX', age=20, score=100)
json_d = json.dumps(d, indent=2)

print(json_d)