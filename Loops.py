#Loops
'''
1. While
2. for
'''

i = 985
x = 0
"""
while x <=10:
    print(f" {i} X {x} = {i*x}")
    x += 1
"""

a = list(range(10))
print(a)

for i in range(10):
    print(f"i is {i}")
    

l = ["xyz", 32, 5.9, 2000]
for item in l:
    print(item)
    

d = {"name":"xyz", "age":32, "height":5.9, "charge_per_h":2000}
val_x =[]
for item in d.keys():
    print(f"key: {item}")
    print(f"Value: {d[item]}")
    print("")
    if item != "height":
        val_x.append(d[item])
else:
    print("Walk theough is complited")


val_l = [d[item] for item in d.keys() if item != "height"]

print(val_l)
