import json

# json module is used to convert the python code to run in java.


data = '{"value_1":"shashank", "value_2": 349494}'
parsed = json.loads(data)

print(parsed)
print(parsed['value_1'])

data_2 = {"value_1": "shashank", "value_2": ["captain america", "tony"], "value_3": ("AMD", "Intel"), "value_4": False}

js_comp = json.dumps(data_2)
print(js_comp)
# You can see some changes in the "js_comp" like the "False" value is changed as "false" , tuple was also changed.
