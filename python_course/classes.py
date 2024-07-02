# Q: wapp to find the given string is palindrom or not
# i/p: nitin
# i/p: sahil

str1 = input(str("Enter you string: "))
str_lst = list(str1)
print(str_lst)

rev_lst = []

for a in range(1, len(str_lst)+1):
    # print(a)

    abc = str_lst[-a]

    rev_lst.append(abc)
print(rev_lst)
    # print(type(abc)) 

if str_lst == rev_lst:
    print("its palandrom")
else:
    print("Its not")

# 
str1 = input(str("Enter you string: "))
str2 = reversed(str1)
# str2 = str(str2)
# print(str2)

str2 = "".join([i for i in str2])
print(str2)

if str1 == str2:
    print("its palandrom")
else:
    print("Its not")


