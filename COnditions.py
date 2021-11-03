# If Conditions
'''
TF-Table
    T and T = T
    T and F= F
    F and T= F
    F and F = F
    
    T or T = T
    T or F = T
    F or T = T
    F or F = F
    
    
COndition Levels:
    1 Simple If
    2 If ... Else
    3 If ... elif ... else
    4 Nested if
    
Comparition->  ==, !=, <, <=, >, >=
Logical => is, nor, and, or
'''
# Req: What ever the input i have given to the system, that should be 
# evaluvated and return whether it an Odd or even. 

'''
Algo:
    1. Take the input and store in a var.
    **. validate the input. if invalied, print erroe message.
    2. cast the into int.
    3. devide with 2 (find mod of the input)
    4. if the remainder is 0, print Even
    5. if the remainder is 1, print Odd
'''

"""
#1. Take the input and store in a var.
_input = input("Enter some number: ")
i = None

if _input =="":
    print("THe input is empty.")
elif nor _input.isnumeric():
    print("The input is invalied.")
else:
    # 2. cast the into int.
    i = int(_input)
    

if i is nor None :
    if i == 0:
        print("The input is 0. And it is even")
    else:

        # 3. devide with 2 (find mod of the input)
        r = i%2
        
        '''
        # Simple If
        if r == 0 :
            print(f"Teh input {i} is Even.")
        
        if r == 1 :
            print(f"Teh input {i} is Odd.")
        
        '''
        
        # If... else
        if r == 0 :
            print(f"Teh input {i} is Even.")
        else:
            print(f"Teh input {i} is Odd.")
"""




"""
get rank:
    ** validate the input
    -> if score is <35 show as Fail
    -> if score is > or equal to 35 and < 45, show as Regular
    -> if score is > or equal to 45 and < 65, show as Red
    -> if score is > or equal to 65 and < 85, show as Orenge
    -> if score is > or equal to 85 and < 95, show as Green
    -> if score is > or equal to 95 and <= 100, show as Gold
"""


"""
    try: ... except:...
"""


max_score = 100
score = None
i = input("Enter your score:")

output_val = ""



try:
    if i is None or i == "":
        output_val = "Invalide Input."
    else:
        score = int(i)
        if   score > max_score:
                output_val = "Score should not be morethan 100."
        else:
            if score < 35:
                output_val = "Fail"
            elif score >= 35 and score < 45:
                output_val = "Regular"
            elif score >= 45 and score < 65:
                output_val = "Red"
            elif score >= 65 and score < 85:
                output_val = "Orenge"
            elif score >= 85 and score < 95:
                output_val = "Green"
            elif score >= 95:
                output_val = "Gold"

except Exception as e:
     output_val = e
finally:
    if score is not None:
        print(f"Score: {score}")
        print(f"Rank House: {output_val}")
    else:
        print(f"Error: {output_val}")
    
    
"""

a=10

r = a%2
if r==0:
    print("Even")
else:
    print("Odd")
    
r = "Even" if a%2 == 0 else "Odd"
print(r)

"""


























