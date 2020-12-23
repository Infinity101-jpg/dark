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
import random as r
def random(x, y):
  return r.randint(x, y)
def write(a):
    print("  --> " + str(a))
def read(b):
    input(b)
read = input
def lengthof(x):
  return(len(x))
def run():
    main()
    print("  --> Process Has Completed.")
'''
with open('o.py', 'w') as filew:
    filew.write(stra + file_contents + "\n\n")

import os
os.system('python o.py')
