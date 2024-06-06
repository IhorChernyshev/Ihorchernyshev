import keyword
import string
my_name = input("print_name: ")
name1 = True
if my_name in keyword.kwlist:
    name1 = False
if my_name.count('__') >= 1:
    name1 = False
if my_name[0].isdigit():
    name1 = False
for qwe in my_name:
    if qwe.isupper() or qwe.isspace() or (qwe in string.punctuation and qwe != '_'):
        name1 = False
print(name1)
