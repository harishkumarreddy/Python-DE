# String
my_value = "A banana in the basket."

'''
print(my_value)
print(my_value[2:10])
print(my_value[2:])
print(my_value[:10])
print(my_value[::3])
print(my_value[::-1])

x = "10"
y = "5"

print(x,y)
print(type(x),type(y))

print(x+y)

x = int(x)
y = int(y)
print(x+y)
print(type(x),type(y))

z = str(x+y)
print(type(z), z)


words = my_value.split(" ", 2)
print(type(words), words)

new_str = "_".join(words)
print(new_str)

print( my_value.upper() )
print( my_value.lower())
'''















'''


words_l = my_value.split(" ")
words_t = tuple(words_l)
words_s = set(words_l)

print(type(words_l), words_l)
print(type(words_t), words_t)
print(type(words_s), words_s)

print(" ".join(words_s))

user_d = {
        "name": "xyz", 
        "age": 32, 
        "Tech": "IT", 
        "charge_per_h": 2000
    }

print(user_d)

print(list(user_d))

_keys = user_d.keys()
_vals = user_d.values()

print(list(_keys))
print(_vals)

'''

'''
words_l = my_value.split(" ")
print(words_l)

print(words_l.count("in"))

print( len(words_l) )
print( len(my_value) )
'''

'''
print(my_value[-10: -5])

words_l = my_value.split(" ")

print(words_l)

words_l.insert(3, "Test")

print(words_l)

words_l.append("Test")

print(words_l)

x_val = words_l.pop(3)
print(words_l)
print(x_val)

words_l.remove("banana")
print(words_l)


words_l2 = my_value.split(" ")

print(words_l)
print(words_l2)

words_l.extend(words_l2)

print(words_l)

'''



user_d = {
        "name": "xyz", 
        "age": 32, 
        "Tech": "IT", 
        "charge_per_h": 2000
    }

print(user_d)

user_d["score"] = 4.6

print(user_d["age"])

x_val = user_d.pop("age")
print(user_d)
print(x_val)

print(user_d.get("age", 0))










































