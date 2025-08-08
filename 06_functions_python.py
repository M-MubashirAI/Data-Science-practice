
# A function is a block of code with only runs when it is called.callable
# You can pass data, known parameters, into a function.
# Functions can return data as a result.

# In python, a function is defined using the def keyword.


# let's define function
def greet_user():
    print("Hello,User")
greet_user()

def aoa():
    print("Assalam O Alaikunm! hey from landon")
aoa()
# # you can pass arguments to a function

def aoa(name):
    print(f"Assalam O Alaikunm! hey from {name}!, kaifa Haluka?")
aoa("Imran khan")

def aoa(name = "Mery piyare bandy"):
    print(f"Assalam O Alaikunm! hey from {name}!, kaifa Haluka?")   

aoa()

def sequare(number):
    return number**2
result = sequare(5)
print(result) 


# lambda function

a = lambda b: b * 10
print(a(10))

















