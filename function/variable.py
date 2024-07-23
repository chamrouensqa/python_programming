Var = "This is variable name"
print(Var)

# Local Variable
def f():
    s = "This is local variable name"
    print(s)
f()

# Global Variable
def g():
    print(glob)
glob = "This is global variable name"
g()

# Global variable scope
x = 100
def change():
    global x
    x = x + 100
    print("This is local variable value ",x)
change()
print("This is outside variable value ",x)

# Create a set
set1 = set("abcdefgh")
print("This is a set ",set1)

# Create Dictionary
Dict = {1:'Sopheak', 2:'Dara', 3:'Makara'}
print("The dictionary of student is ",Dict)