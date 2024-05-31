first_list = [52,14,33,10]
if len(first_list) == 0:
    print(first_list)
else:
    a = first_list.pop()
    first_list.insert(0,a)
    print(first_list)