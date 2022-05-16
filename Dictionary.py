
d1 = {}
print(type(d1))
d2 = {"Shashank": "Shekhar", "Shekhar": {"Singh": "39", "Golu": "20"}}
print(d2)
print(d2["Shashank"])
print(d2["Shekhar"])
print(d2["Shekhar"]["Singh"])
print(d2.keys())
d2["Captain"] = "Steve"
d2["Tony"] = "Stark"
print(d2)
del d2["Tony"]
print(d2)
d3 = d2
print(d3["Shashank"])

#--- copy of d2
d3 = d2.copy()
print(d3["Shashank"])


print(d2.get("Shashank"))
d2.update({"Thor":"Odinson"})
print(d2)
print(d2.keys())
print(d2.items())

