import random
import time
import tracemalloc

class Sortirovki_cpython:

    def __init__(self, lis):
        self.lis = lis

    def list_random(n):
        return random.sample(range(0, n), n)

    def list_normal(n):
        return [i for i in range(0, n)]

    def list_reverse(n):
        return [i for i in range(0, n)][::-1]

    def list_almost(n):
        numSort = int(n * 0.95) + 1
        if numSort == n:
            return Sortirovki_cpython.list_normal(n)[numSort-1:] + Sortirovki_cpython.list_normal(n)[:numSort-1]
        else:
            return Sortirovki_cpython.list_normal(n)[numSort-1:] + Sortirovki_cpython.list_normal(n)[:numSort]



    def bubble_sort(self):
        tracemalloc.start()
        on = time.perf_counter()
        for _ in range(0, len(self.lis) - 1):
            for i in range(0, len(self.lis) - 1):
                if self.lis[i] > self.lis[i+1]:
                    self.lis[i], self.lis[i+1] = self.lis[i+1], self.lis[i]
        tw = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        peak_bytes = peak[1]
        tracemalloc.stop()
        time_rec = (tw - on) * 1000
        memor_kb = peak_bytes / 1024
        return time_rec, memor_kb

    def insertion_sort(self):
        tracemalloc.start()
        on = time.perf_counter()
        for i in range(0, len(self.lis)):
            key = self.lis[i]
            j = i - 1
            while j >= 0 and key < self.lis[j]:
                self.lis[j+1] = self.lis[j]
                j -= 1
                self.lis[j+1] = key
        tw = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        peak_bytes = peak[1]
        tracemalloc.stop()
        time_rec = (tw - on) * 1000
        memor_kb = peak_bytes / 1024
        return time_rec, memor_kb


    def selection_sort(self):
        tracemalloc.start()
        on = time.perf_counter()
        lis_result = []
        for _ in range(0, len(self.lis)):
            el_min = min(self.lis)
            lis_result.append(self.lis.pop(self.lis.index(el_min)))
        tw = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        peak_bytes = peak[1]
        tracemalloc.stop()
        time_rec = (tw - on) * 1000
        memor_kb = peak_bytes / 1024
        return time_rec, memor_kb

    def quick_sort(self):
        tracemalloc.start()
        def quick_sorttt(lis):
            if len(lis) <= 1:
                return lis
            opor = random.randrange(1, len(lis))
            left = [i for i in lis if lis[opor] > i]
            middle = [i for i in lis if lis[opor] == i]
            right = [i for i in lis if lis[opor] < i]
            return quick_sorttt(left) + middle + quick_sorttt(right)

        on = time.perf_counter()
        self.lis = quick_sorttt(self.lis)
        tw = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        peak_bytes = peak[1]
        tracemalloc.stop()
        time_rec = (tw - on) * 1000
        memor_kb = peak_bytes / 1024
        return time_rec, memor_kb

    def merge_sort(self):
        tracemalloc.start()
        def merge_sorttt(lis):
            if len(lis) <= 1:
                return lis
            mid = len(lis) // 2
            left = merge_sorttt(lis[:mid])
            right = merge_sorttt(lis[mid:])
            return merge(left, right)
      

        def merge(left, right):
            res = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res

        on = time.perf_counter()  
        self.lis = merge_sorttt(self.lis)
        tw = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        peak_bytes = peak[1]
        tracemalloc.stop()
        time_rec = (tw - on) * 1000
        memor_kb = peak_bytes / 1024
        return time_rec, memor_kb

    def heapp(self, n, i):
        tracemalloc.start()
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.lis[left] > self.lis[largest]:
            largest = left
        if right < n and self.lis[right] > self.lis[largest]:
            largest = right
        if largest != i:
            self.lis[i], self.lis[largest] = self.lis[largest], self.lis[i]
            self.heapp(n, largest)

    def heap_sort(self):
        on = time.perf_counter()
        n = len(self.lis)
        for i in range(n // 2 - 1, -1, -1):
            self.heapp(n, i)
        for i in range(n - 1, 0, -1):
            self.lis[i], self.lis[0] = self.lis[0], self.lis[i]
            self.heapp(i, 0)

        tw = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        peak_bytes = peak[1]
        tracemalloc.stop()
        time_rec = (tw - on) * 1000
        memor_kb = peak_bytes / 1024
        return time_rec, memor_kb


    def counting_sort(self):
        tracemalloc.start()
        on = time.perf_counter()
        if not self.lis:
            return self.lis
        min_val, max_val = min(self.lis), max(self.lis)
        counts = [0] * (max_val - min_val + 1)
        for num in self.lis:
            counts[num - min_val] += 1
        res = []
        for index, count in enumerate(counts):
            res.extend([index + min_val] * count)

        tw = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        peak_bytes = peak[1]
        tracemalloc.stop()
        time_rec = (tw - on) * 1000
        memor_kb = peak_bytes / 1024
        return time_rec, memor_kb

    def radix_sort(self):
        tracemalloc.start()
        on = time.perf_counter()
        if not self.lis:
            return self.lis
        min_val = min(self.lis)
        if min_val < 0:
            self.lis = [x - min_val for x in self.lis]
        max_num = max(self.lis)
        place = 1
        while max_num // place > 0:
            buckets = [[] for _ in range(10)]
            for num in self.lis:
                digit = (num // place) % 10
                buckets[digit].append(num)
            self.lis = []
            for bucket in buckets:
                self.lis.extend(bucket)
            place *= 10
            
        if min_val < 0:
            self.lis = [x + min_val for x in self.lis]

        tw = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        peak_bytes = peak[1]
        tracemalloc.stop()
        time_rec = (tw - on) * 1000
        memor_kb = peak_bytes / 1024
        return time_rec, memor_kb

    def bucket_sort(self):
        tracemalloc.start()
        on = time.perf_counter()
        if len(self.lis) <= 1:
            return self.lis  
        max_val = max(self.lis)
        min_val = min(self.lis)
        if min_val == max_val:
            return self.lis
        range_val = max_val - min_val
        buck = [[] for _ in range(len(self.lis))]
        for num in self.lis:
            index = int((num-min_val) / range_val * (len(buck) - 1))
            if index >= len(self.lis):
                index -= 1
            buck[index].append(num)
        res = []
        for i in range(len(buck)):
            buck[i].sort()
            res.extend(buck[i])

        tw = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        peak_bytes = peak[1]
        tracemalloc.stop()
        time_rec = (tw - on) * 1000
        memor_kb = peak_bytes / 1024
        return time_rec, memor_kb


    def __del__(self):
        pass


