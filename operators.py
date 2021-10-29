'''
Operators:
    1. Assignment -> =
    2. Arithmatic -> +,-,*,/,%,**
    3. Comparition->  ==, !=, <, <=, >, >=
    4. Logical => is, not, and, or
    5. Bitwise => <<, >>
    
    
    TF-Table
    T and T = T
    T and F= F
    T or T = T
    T or F = T
    F and F = F
    F or F = F
    
'''

# Assignment"
my_val = "somedata"

#  Arithmatic
x,y = 10, 5

print( x+y )
print( x-y )
print( x*y )
print( x/y )
print( x%y )
print( x**y )

print( x//y )

print("")
# Comparition
print( x == y )
print( x != y )
print( x < y )
print( x <= y )
print( x > y )
print( x >= y )
print("")

# Logical
print( x is y )
print( x is not y )
print( x>y and y<=10 )
print( x>y or y<=10 )