def factorial(n):
    if n == 1:
        return 1
    factorial_n_1 = factorial(n=n - 1)
    return n * factorial_n_1

print(factorial(int(input('Введите число: '))))
