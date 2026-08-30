import time
import random


on = time.time()

lis_random = random.sample(range(0,20_000), 20_000)
lis_normal = [i for i in range(0, 20_000)]
lis_result = []

def func(lis:list):
    for i in range(0, len(lis)):
        el_min = min(lis)
        lis_result.append(lis.pop(lis.index(el_min)))
    return lis_result

print(func(lis_random))
tw = time.time()
print(f'Время выполнения: {tw - on}')