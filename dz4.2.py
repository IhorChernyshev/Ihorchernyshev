lst = [1,2,3,4,5]
i = 0
lst1 = []
if lst:
    i = 0
    while i < len(lst):
        x = lst[i]
        i += 2
        lst1.append(x)
        y = lst[-1]
        continue
    print(sum(lst1) * y )
else:
    print(lst1)

