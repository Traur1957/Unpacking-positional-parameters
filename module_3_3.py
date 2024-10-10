def print_params(a=1, b='String', c=True):
    print(a, b, c)


print_params()
print_params(c=True)
print_params(b=25, c=[1, 2, 3])

values_list = [5, 'Sun', 6.3]
values_dict = {'a': 2, 'b': 'Moon', 'c': 7.1}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [10, 'Earth']

print_params(*values_list_2, 42)