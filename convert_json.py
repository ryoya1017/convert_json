import json

json_file = open('sample.json', 'r', encoding='utf-8')
json_str=json_file.read()
json_str = json_str.replace('\\', '/')
print(json_str)
json_object = json.loads(json_str)
objects_name=[]

#print(json_object[0]["objects"][0]["name"])
#print(json_object[0]["objects"][1]["name"])
#print(json_object[0]["objects"][2]["name"])
#print(json_object[0]["objects"][3]["name"])


for w in json_object[0]["objects"]:
#    print(w["name"])
    objects_name.append(w["name"])

filename = 'objects.json'

with open(filename, 'w') as f:
    json.dump(objects_name, f)

#object_json=json.dumps(object_name)
#print(object_json)
