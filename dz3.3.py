first_list1 = [1,2,3,4,5]
a = len(first_list1)
x = (a + 1) // 2
second_list1 = first_list1[0:x]
third_list1 = first_list1[x:]
fourth_list1 = []
fourth_list1.append(second_list1)
fourth_list1.append(third_list1)
print(first_list1)
print(fourth_list1)