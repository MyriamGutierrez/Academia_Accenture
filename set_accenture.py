my_list1 = [1, 3, 6, 24, 78, 35, 55]
my_list2 = [12, 24, 35, 24, 88, 120, 155]

a = set(my_list1)
b = set (my_list2)

c = set(a & b)
res_list = list(c)
print res_list