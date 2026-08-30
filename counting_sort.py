import random
import time

lis_random = random.sample(range(0, 1_000_000), 1_000_000)
lis_normal = [i for i in range(0, 10)]

on = time.perf_counter()

def counting_sort(lis):
    if not lis:
        return lis
    min_val, max_val = min(lis), max(lis)
    counts = [0] * (max_val - min_val + 1)
    for num in lis:
        counts[num - min_val] += 1
    res = []
    for index, count in enumerate(counts):
        res.extend([index + min_val] * count)
    return res


counting_sort(lis_random)
tw = time.perf_counter()
print(f'Время выполнения: {tw - on}')


