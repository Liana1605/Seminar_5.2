#Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, .., .and
#где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#Требуется найти N-е число Фибоначчи
#Input: 7
#Output: 21

def fib(n: int) -> int:
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(int(input('Введите целое число: '))))
