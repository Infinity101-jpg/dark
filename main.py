with open('main.dark', 'r') as file:
    file_contents = file.read()
stra = '''
print(" " * 15000)

def typeof(z):
    if type(z) == int:
        return 'Intiger';

    if type(z) == float:
        return 'Float';

    if type(z) == str:
        return 'String';

    if type(z) == bool:
        return 'Boolean';
true = True
false = False

def write(a):
    print("  --> " + str(a))
def read(b):
    input(b)
    
    
def run():
    main()
    print("  --> Process Has Completed.")
'''
with open('o.py', 'w') as filew:
    filew.write(stra + file_contents + "\n\n")

import os
os.system('python o.py')
