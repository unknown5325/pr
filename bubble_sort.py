import random
import time

lis_random = [random.randint(0, 10_000) for _ in range(0, 10_000)]
lis_normal = [i for i in range(0, 20_000)]
   
on = time.time()
def func(lis):
    for _ in range(0, len(lis) - 1):
        for i in range(0, len(lis) - 1):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]

print(func(lis_random))
tw = time.time()
print(f'Время выполнения: {tw - on}')
