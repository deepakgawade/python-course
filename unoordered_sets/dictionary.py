thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["color"]="Blue"

print(thisdict)

for x,y in thisdict.items():
    print(x,y)

for y in thisdict:
    print(thisdict[y])

for x in thisdict:
    print(x)