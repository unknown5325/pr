import random
import time

lis_random = random.sample(range(0, 1_000_000), 1_000_000)
lis_normal = [i for i in range(0, 10)]

on = time.perf_counter()

def bucket_sort(lis: list):
    if len(lis) <= 1:
        return lis  
    max_val = max(lis)
    min_val = min(lis)
    if min_val == max_val:
        return lis
    range_val = max_val - min_val
    buck = [[] for _ in range(len(lis))]
    for num in lis:
        index = int((num-min_val) / range_val * (len(buck) - 1))
        if index >= len(lis):
            index -= 1
        buck[index].append(num)
    res = []
    for i in range(len(buck)):
        buck[i].sort()
        res.extend(buck[i])
    return res

tw = time.perf_counter()

bucket_sort(lis_random)
tw = time.perf_counter()
print(f'Время выполнения: {tw - on}')