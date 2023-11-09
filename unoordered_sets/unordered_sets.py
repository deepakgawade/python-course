setA={"A","B","C",2,12}
print(type(setA))

setB=set([1,12,2,3,2,1,1,2])

print(setB)

setB.add(40)
print(setB)

setB.remove(2)
print(setB)

all= setA.union(setB)

print(all)


common=setA.intersection(setB)

print(common)

print("A" in setA)