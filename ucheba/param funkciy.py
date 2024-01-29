def print_params(a=6, b='Oleg', c=True):
    return a, b, c


res = print_params(a=6, b='Oleg', c=True)
print(res)

res = print_params()
print(res)

res = print_params(a=8)
print(res)

res = print_params(a=8, b=25, c=[1,2,3])
print(res)

res = print_params(b=26)
print(res)

values_list = [2, 3, 4]
res = print_params(*values_list)
print(res)

values_dict = {'a': 2, 'b': 'Frolov', 'c': False}
res = print_params(**values_dict)
print(res)

values_list = [2, 3]
values_dict = {'c': False}
res = print_params(*values_list, **values_dict)
print(res)

values_list_2 = ['Victor', False]
res = print_params(*values_list_2, 42)
print(res)
