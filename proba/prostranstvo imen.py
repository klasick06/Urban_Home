c, d = 1, 2
print('Global:', c, d)


def test():
    a, b = 3, 4
    print('test:', a, b)


def test_2(x, y, z):
    print(x, y, z)


test()
test_2(10, 11, 20)
