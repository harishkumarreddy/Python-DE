# Functions / Methods
'''
    1. Pre-definded
    2. User-defiended
    3. Lamda
    
    Case-sencitivity => a != A
    Case-in-sencitivity => a == A
'''

'''
def sayHello():
    print("Hello World")    


# with argument / parameter
def sayHello1(in_text):
    print(f"Hello {in_text}!")

sayHello()
sayHello1("Harish")
sayHello1("Manu")
sayHello1("Akash")
print("=" * 50)

'''

'''
def wish(w_name, w_time="m"):
    msg = "Good Morning"
    
    if w_time == "a":
        msg = "Good Afternoon"
    elif w_time == "e":
        msg = "Good Evening"
    elif w_time == "n":
        msg = "Good Night"
        
    print(f"Hello {w_name}, {msg}.")
    
wish("Harish", "m")
wish("Manu", "a")
wish("Akash", "e")
wish("Harish", "n")
wish("Harish")

wish("a","Harish")
wish(w_time="a",w_name="Harish")
'''

'''
    1. Args  => *args
    2. Kwargs => **kwargs
'''


'''
def setUserAccess(uid, *args):
    print(uid)
    print(type(args), args)

def setUserAccess2(uid, **modules_list):
    print(uid)
    print(type(modules_list), modules_list)
    
def setUserAccess3(uid, **modules_list):
    output_val = {
            "UID": uid,
            "Access_list":  modules_list
        }
    
    return output_val

setUserAccess(
    "harish", 
    "CRUD", 
    "Reportes", 
    "Billing", 
    "DBA", 
    "Security")
setUserAccess2(
    uid="harish", 
    module1="CRUD", 
    module2="Reportes", 
    module3="Billing", 
    module4="DBA", 
    module5="Security")

user_access = setUserAccess3(
    uid="harish", 
    module1="CRUD", 
    module2="Reportes", 
    module3="Billing", 
    module4="DBA", 
    module5="Security")

print(user_access)

'''


'''
=> lAMDA -> Single line function

'''


is_even = lambda a: not bool(a%2)

getTimesVal = lambda x,y: x*y 

res = is_even(3)
print(res)

print(getTimesVal(108,999))





































