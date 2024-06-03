lst = [4, 0, 8, 0, 0, 5, 6, 0, 3, 0, 32]
i = 0
while i < len(lst):
    l = lst[i]
    i += 1
    if l != 0:
        continue
    lst.remove(l)
    lst.append(l)
print(lst)
