import random
import time

lis_random = random.sample(range(0, 1_000_000), 1_000_000)
lis_normal = [i for i in range(0, 10)]

on = time.perf_counter()


def radix_sort(lis):
    if not lis:
        return lis
    min_val = min(lis)
    if min_val < 0:
        lis = [x - min_val for x in lis]
    max_num = max(lis)
    place = 1
    while max_num // place > 0:
        buckets = [[] for _ in range(10)]
        for num in lis:
            digit = (num // place) % 10
            buckets[digit].append(num)
        lis = []
        for bucket in buckets:
            lis.extend(bucket)
        place *= 10
        
    if min_val < 0:
        lis = [x + min_val for x in lis]
    return lis

radix_sort(lis_random)
tw = time.perf_counter()
print(f'Время выполнения: {tw - on}')