""" An example Python script
 Note that triple quotes allow multiline strings
"""
# single line comments are indicated with a "#"
import sys # loads the sys (system) library

def aVidhyaFunction(a,b,c):
    """ This is my first function """
    print(f"hello vidhya how are you {a} {b} {c}" )
def varArgs(**args):
    """ This is my first function """
    print(f"hello vidhya how are you {args}" )
def varArg(*args):
    """ This is my first function """
    print(f"hello vidhya how are you {args}" )


def main_function(parameter):
 """ This is the docstring for the function """
 print ("here is where we do stuff with the parameter")
 print (parameter)
 return parameter # this could also be multiples
if __name__ == "__main__":
 """ this will only be true if the script is called
 as the main program """
 # command line parameters are numbered from 0
 # sys.argv[0] is the script name
 param = sys.argv[1] # first param after script name
 # the line below calls the main_function and
 # puts the result into function_result
 function_result = main_function(param)
 print (function_result)

 for item in ['spam', 'spam', 'spam', 'spam']:
     print (item)

for item in range(4, 10, 2):
    print (item)

try:
    xValue = 1
    item = xValue
    some = (19,29,292)
    keyValue = {1:'vidhya'}
    v = 2**4
    print (v)
except TypeError:
    print("x isn't a list")
except NameError:
    print("x is not defined test")
except IndexError:
    print("index out of range")
else:
    print("no exception raised")
finally:
    print("processing complete")
    aVidhyaFunction(10,20,200)
    varArgs(c=10,a=20,b=200)
    varArg(20,29,92)
    

