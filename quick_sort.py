import time
import random

lis_random = [random.randint(0, 20_000) for _ in range(0, 20_000)]
lis_normal = [i for i in range(0, 20_000)]
on = time.time()

def func(li):
    if len(li) <= 1:
        return li
    opor = random.randrange(1, len(li))
    left = [i for i in li if li[opor] > i]
    middle = [i for i in li if li[opor] == i]
    right = [i for i in li if li[opor] < i]
    return func(left) + middle + func(right)

a = func(lis_random)
print(a)

tw = time.time()
print(f'Время выполнения: {tw - on}')

