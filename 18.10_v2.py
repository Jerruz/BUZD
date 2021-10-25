import random

# ls = [['k1', 1], ['k2', 2], ['k3', 3]]
# my_dic = dict(ls)
# print(my_dic)


r_nums = {random.randint(1, 100) for i in range(10)}

print(r_nums)
