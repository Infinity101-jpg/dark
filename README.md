# Dark
The Dark Programming Language (runs off of Python).

All of your code runs in the "main.dark" file. Do not edit the "main.py" file. Also, do not edit the "o.py" file. These files make the Programming Language work, so do not edit them. Note: variable name cannot be "pass" use "passw" instead. When running the program, do not open the "main.dark" file when trying to run your program. You must write your code in the "main.dark" file, but when running it, open the "main.py" file.

# How To Write Your First Program
Below is a simple "Hello World" program.

def main():
	write('Hello, World!')
		
run()

As you can see, the Dark Programming Language is a very simple language.

# How To Make A Loop
Below is a simple loop.

def main():
	i = 1
	while i <= 10:
		print(i)
		i = i + 1

run()

# Data Types
Below is all The data types.

int:
a = 10

float:
b = 2.4

str:
c = "Hello, World!"

boolean:
d = true
e = false

*Note when writing a boolean, everything is in lowercase letters.

# How to check what the type of something is

def main():
	a = 10
	write(typeof(a))

run()

/or/

def main():
	write(typeof("Hello"))

run()

/or/

def main():
	write(typeof(true))

run()

/or/

def main():
	write(typeof(1.5))

run()

# If/Else Statements

def main():
	a = 'hello'
	if a == 'hello':
		write('hi');
	else:
		write('oops');

run()

# How To Check For Type

def main():
	write(typeof("Hello"))

run()

# How to define a function
NOTE THAT YOU CANNOT DEFINE ANOTHER FUNCTION INSIDE THE MAIN() FUNCTION. DEFINE ANOTHER FUNCTION OUTSIDE OF THE MAIN FUNCTION FOR EXAMPLE:
def main():
	add(3, 6)

def add(a, b):
	write(a + b)
run()

NOT:

def main():
	def add(a, b):
		write(a + b)

	add(3, 9)


run()

It can tecnically work with some instances, but not all. So please define other functions outside of the main()
 function.
