import time
import random


on = time.time()
lis_random = random.sample(range(0, 100_000), 100_000)
lis_normal = [i for i in range(0, 20_000)]

def func(lis):
    for i in range(0, len(lis)):
        key = lis[i]
        j = i - 1
        while j >= 0 and key < lis[j]:
            lis[j+1] = lis[j]
            j -= 1
            lis[j+1] = key
    return lis

print(func(lis_random))
tw = time.time()
print(f'Время выполнения: {tw - on}')