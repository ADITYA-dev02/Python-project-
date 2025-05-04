from list1 import append1, extend1, pop0, remove1
from set2 import slen2, adds2, remove2
from dict3 import len3, add3, keys30, values30

my_list = [1, 2, 3]
print("Append 4:", append1(my_list, 4))
print("Extend [5, 6]:", extend1(my_list, [5, 6]))
print("Pop:", pop0(my_list))
print("Remove 2:", remove1(my_list, 2))
my_set = {1, 2, 3}
print("Length of set:", slen2(my_set))
print("Add 4 to set:", adds2(my_set, 4))
print("Remove 2 from set:", remove2(my_set, 2))

my_dict = {'a': 1, 'b': 2}
print("Length of dict:", len3(my_dict))
print("Add ('c', 3):", add3(my_dict, 'c', 3))
print("Keys:", keys30(my_dict))
print("Values:", values30(my_dict))