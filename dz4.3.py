import random

lst1 = random.randint(3, 10)
lst2 = [random.randint(3, 10) for i in range(lst1)]
new_list = [lst2[0], lst2[2], lst2[-2]]
print(lst2)
print(new_list)
