data = {}
print(type(data))

data = {"name": "Zack", "Age": "20", "Country": "India"}

print(data)

print(data["name"])

print(data.keys())

data2 = {(1, 2, 3): "Zack"}

print(data2)

data.update(data2)

print(data)
