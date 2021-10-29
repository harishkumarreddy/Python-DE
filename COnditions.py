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
Logical => is, not, and, or
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

#1. Take the input and store in a var.
_input = input("Enter some number: ")
i = None

if _input =="":
    print("THe input is empty.")
elif not _input.isnumeric():
    print("The input is invalied.")
else:
    # 2. cast the into int.
    i = int(_input)
    

if i is not None :
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






























