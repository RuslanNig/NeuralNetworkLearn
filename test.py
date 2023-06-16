#test commit push python file
print("hello git!")

#save it in file mymodule.py
def greeting(name):
    print("Hello, " + name)

import sys
sys.path.append('/Users/Lyceum1557/Pictures/src/')
#main file in dir 'C/Users/Lyceum1557/Pictures/src/'
#mymodule file in subdir src
import mymodule
mymodule.greeting("Ruslan")