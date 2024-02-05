def test(a, b, *args, **kwargs):
    print(test)
    print('a и b:' , a, b)
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('парамметры:', i, arg)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('парамметры:', key, '=', value)


test(6,11, name= 'Oleg', city='Krasnoayrsk')
