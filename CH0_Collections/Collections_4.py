thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"]		    # Mustang (배열처럼 사용)
x = thisdict.get("model")       # Mustang (잘 사용하지 않는 표현)
print(x)
print()

# -------------------

print(len(thisdict))		    # 3
print(thisdict)                 # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

for x in thisdict:
    print(x)			        # brand model year
print()

for x in thisdict:
    print(thisdict[x]) 		    # Ford Mustang 1964
print()

# -------------------

print(thisdict.keys())          # dict_keys(['brand', 'model', 'year'])

for x in thisdict.keys():
    print(x)			        # brand model year
print()

print(thisdict.values())        # dict_values(['Ford', 'Mustang', 2018])

for x in thisdict.values():
    print(x)			        # Ford Mustang 1964
print()

# -------------------

print(thisdict.items())         # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])

for x, y in thisdict.items():
    print(x, y)		            # brand Ford / model Mustang / year 1964
print()

print(list(thisdict.items()))
print()

# -------------------

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the dictionary")
print()

thisdict["year"] = 2018
print(thisdict)                 # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
print()

thisdict["color"] = "red"       # 새로운 key-value 추가
print(thisdict)                 # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'}
print()

del thisdict["model"]
print(thisdict)                 # {'brand': 'Ford', 'year': 2018, 'color': 'red'}
print()

