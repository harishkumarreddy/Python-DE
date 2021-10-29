# Lists -> Mutable

users = [
        "Admin",
        "Test User",
        "Data Entry",
        "Analyst"
    ]

adminUser = [
        "Harishkumar",
        True,
        "IT",
        "03/02/2021",
        "26/10/2021 07:00:00"
    ]


'''
    Indexing:
        Starts with 0
        last item index n-1
            n = length of items

'''

print(users[0])
print(users[1])
print(users[2])
print(users[3])

print(adminUser[3])
print(adminUser[1])


adminUser[1] = False
adminUser[2] = "PMO"
print(adminUser)







# TUPPLE => Immutabule
users_t = (
        "Admin",
        "Test User",
        "Data Entry",
        "Analyst"
    )

# print(users_t[0])
# print(users_t[2])

# users_t[2] = "Billing"

# SET
users_s = {
        "Admin",
        "Test User",
        "Test User",
        "Data Entry",
        "Analyst"
    }

print(users_s)

print(users_s[0])

print(type(users))




# Dict => Mutable

user_d = {
        "name": "xyz", 
        "age": 32, 
        "Tech": "IT", 
        "charge_per_h": 2000
    }


print(type(user_d))

print(user_d)
print(user_d["name"])
print(user_d["age"])
print(user_d["Tech"])
print(user_d["charge_per_h"])

user_d["Tech"] = "IT Sequrity"

print(user_d["Tech"])































