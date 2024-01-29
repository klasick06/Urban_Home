my_cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for car in my_cars:
    if car == 'LADA':
        print('ФУУУ...')
        continue
    print('Я езжу на автомабиле марки', car)
    if car == 'HONDA':
        print('Honda FIT')
    cars_count += 10
print('конец кикла')
