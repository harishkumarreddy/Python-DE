# OI => input & output

'''
    * I/Input => input()
    * O/Output = > Ptint()


x = input("Enter Name: ")

print(x)
'''

'''
FileIO -> input/Output operations on files presented in hard drive.
modes:
    r = read
    w = write
    
    r+ = read and write
    w+ =writ and excute
    
    a = append to end of the file
    a+ = append and read

'''


fs = open(r"D:\Projects\PPS\Python\b2\test.text", "r");
data = fs.read()
print(data)

lines = fs.readlines()
print(lines)

fs.close();

#fs = open(r"D:\Projects\PPS\Python\b2\test2.text", "w");
fs = open(r"D:\Projects\PPS\Python\b2\test2.text", "a");

fs.write("hello-World\n")

fs.write("hello-World\n")

fs.write("hello-World\n")

fs.close()






























