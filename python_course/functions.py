print("India")
print("USA")
print("UK")

# funtions can be written once and used multiple times
def print_name(name):
    print(name)


print_name("America")
print_name("India")
print_name("Uk")

#######################

def addition(a,b):
    c = a + b
    print(c)

addition(2, 3)

#######################

# funtions can return some value and it could be used to assigne to any variable where we are calling funtion

def addition(a, b):
    c = a + b
    return c

def multiply(a, b):
    c = a * b
    return c

oppa = addition(2, 3)
print(oppa)

c = multiply(oppa, 3)
print(c)

########################

def division(a, b):
    c = a/b
    return c

c = division(2, 3)
print(c)

########################

# we can assign some default values to the parameters
# so that even if the function is called without providing parameter it will run

def addition(a=2, b=3):
    print(a,b)
    c = a + b
    return c

d = addition()
print(addition())

########################

# If there is default value assigne to parameter we can pass some new value to them while calling function

ad = addition(a=5, b=8)
print(ad)

ad = addition(8, 5)
print( ad)

ad = addition(10)
print(ad)

ad = addition(a =10)
print(ad)

ad = addition(b = 10)
print(ad)


#########################

# required parameters always need to be on left side i.e. eg (a, c, d, b=3, f=9, g=18)
# so this should not be like (a = 10, b, c) << wrong way

def addition(a, b=3):
    print(a, b)
    c = a+b
    return c

ad = addition(2)
print(ad)
ad = addition(a=2)
print(ad)

ad = addition(2, b=4)
print(ad)


# required positional arguments should always before default positional argument

def addition(b, a=2):
    print(a, b)
    c= a+b
    return c

ad =addition(2, 3)
print(ad)

ad = addition(2, 3)
print(ad)

# non-default argument follows default argument

def addition(d, f, g, h, a=3, b=2):
    print(a, b)
    c = a+b
    return c

ad = addition(2,3,4,5,6,8)
ad = addition(2,3,4,5,a=6,b=8)
print(ad)

#########################################################################################

def addition(a, b):
    print(a, b)
    c = a +b
    return c

c = addition("space", "story")
print(c)

def addition(a:int, b:int):
    print(a,b)
    c = a+b
    return c

c = addition("space", "story")
print(c)
c = addition(10,12,11,15)
print(c)

c = addition("shraddha", 17.75)
print(c)

def addition(a:int, b:int):
    if str(type(a)) != 'int':
        return "input a has to be integer"
    print(a, b)
    c = a + b
    return c

c = addition("space", 17.75)
print(c)



def addition(a,b):
    print(a,b)
    p = 10
    def multiply(a,b):
        print(a, b)
        z = 1000
        m = a*b
        return m
    c = a + b
    m = multiply(a, b)
    return c, m

c, m = addition(2, 3)

print(c, m)


#################################################################################

# use of global variable

def sample():
    p = 10
    def sample_1():
        z = 100
        return z
    z = sample_1()
    print(z)

sample()


# can use global variable inside a funtion only

def sample():
    global z
    z = 100

sample()
print(z)

def sample():
    """
    this is sample funtion
    """
    z = 100


# sample()

print(sample.__doc__)

print(vars(sample))


#############################################################################

# recursive funtions

def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)

value = fact(5)
print(value)