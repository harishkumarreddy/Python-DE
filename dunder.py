'''
Dunder Methods -> double underscore Methoads
 ex: __metoad_name__ 
 
'''

def main():
    x = input("Enter number to print the table:")
    if x =="" or x is None or not x.isnumeric():
        print("Invalied input. Try again.")
        return True
    
    x = int(x)
    for i in range(0, 11):
        print(f"{x} X {i} = {x*i}")
        
    print("Executin finished.")


if __name__ == "__main__":
    main()