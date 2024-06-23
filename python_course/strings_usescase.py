# strings

"""
int: 1,2,3,4,5,78,231,465
str: "[A-Z]abcdefghijklmnopqrstuvwxyz" whatever inside "" or '' is string
float: 1.23343434, 23.443, 3.14
complex number: 2 + 3i
"""

print("[sdasda3474927492748297493()}{}]")

some_num = 23
some_value = 3.14
complex_num = complex(2 + 3*1j)
boolien = bool(True)
print(complex_num)

#--------------- Strings ---------------#
#conversion of anything into string

some_str = str(some_num)
print(some_str)
print(type(some_str))
print(type(some_num))
print(type(some_value))
print(type(complex_num))

some_str = str(some_value)
print(some_str, type(some_str))

#--------------- Strings ---------------#
some_string = "123456789"
print(some_string[0])
print(some_string[-1])
print(some_string[0:9])
print(some_string[0:4])

print(some_string[0:9:2])
print(some_string[0:4:3])

print(some_string.isalpha())
some_string = "shraddha"
print(some_string.isalpha())
some_string = "shraddha2311"
print(some_string.isalpha())
print(some_string.isalnum())

# string conversions

some_string = "SHRADDHA"
print(some_string.lower())

some_string = "shraddha"
print(some_string.upper())

print(some_string.capitalize())

some_string = "shraddha abhang"
print(some_string.startswith("sh"))
print(some_string.startswith("h"))

print(some_string.endswith("ha"))

some_val = "ad" in some_string
print(some_val)

count = some_string.count("d")
print(count)

idx = some_string.find("h")
print(idx)
some_string = "shraddha abhang"
print(some_string.strip())
print(some_string.rstrip())

some_string = "shraddha ABHANG"
print(some_string.replace(" ", ""))

print(some_string.split())
print(some_string.swapcase())
print(some_string.title())
# lower, upper, string, rstrip, replace, split, swapcase

#--------------- Strings ---------------#
some_string = "shraddha"
some_string += "abhang"
some_string = some_string + " abhng"

new_string = f"{some_string} abhang"
print(new_string)

new_str = "{} {}".format("shraddha", "abhang")
print(new_str)

for i in some_string:
    print(i)

# float > int
num = 3.141518
print(num)
print(int(num))

print(round(num, 4))

num = 5
print(float(num))