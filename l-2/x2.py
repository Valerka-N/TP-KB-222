d = {'l': 1, 'e': 4}
new_d = {'e': 2, 'a': 3}
d.update(new_d)
print(d)  

d2 = {'l': 1, 'e': 2, 'r': 3}
del d2['l']
print(d2)  

d3 = {'l': 1, 'e': 2, 'r': 3}
d3.clear()
print(d3) 

d4 = {'l': 1, 'e': 2, 'r': 3}
k = d4.keys()
print(k)  

d5 = {'l': 1, 'e': 2, 'r': 3}
v = d5.values()
print(v)  

d5 = {'l': 1, 'r': 2, 'a': 3}
i = d5.items()
print(i)  