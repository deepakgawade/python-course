import numpy as np

lst = [23,354,354,56,78,89]
lst3=[1,2,3,4,4,5]
print(lst)
print(type(lst))
vctor = np.array(lst)
vctor4 = np.array(lst3)
vctor[0]=12
vctor.put(0,10)

#vctor.fill(50)
#horizontal vector
print(type(vctor))

lst2=[[12],[23],[3],[80],[67]]

#vertical vector
vctor2=np.array(lst2)
print(vctor)
print(vctor2)
vctor3=vctor+vctor2
vctor5=vctor4+vctor
print(vctor5)
# Addition
# Subtraction
# Multiplication
# Division
# Dot Product, etc.


