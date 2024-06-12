import string

a = input("Enter two letters separated by a hyphen, for example, ('a-z'): ")
start, end = a.split('-')
start_index = string.ascii_letters.index(start)
end_index = string.ascii_letters.index(end)
print(string.ascii_letters[start_index:end_index+1])
