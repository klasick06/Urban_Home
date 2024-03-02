def test_function():
    print('test_function')
    inner_function()

def inner_function():
        print('Я в области видимости функции', test_function)

inner_function()
