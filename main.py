from class_pypy import Sortirovki_pypy

lis_normal_10 = Sortirovki_pypy.list_normal(10)
lis_normal_500 = Sortirovki_pypy.list_normal(500)
lis_normal_1000 = Sortirovki_pypy.list_normal(1_000)
lis_normal_50000 = Sortirovki_pypy.list_normal(50_000)
lis_normal_1000000 = Sortirovki_pypy.list_normal(1_000_000)

lis_random_10 = Sortirovki_pypy.list_random(10)
lis_random_500 = Sortirovki_pypy.list_random(500)
lis_random_1000 = Sortirovki_pypy.list_random(1_000)
lis_random_50000 = Sortirovki_pypy.list_random(50_000)
lis_random_1000000 = Sortirovki_pypy.list_random(1_000_000)

lis_reverse_10 = Sortirovki_pypy.list_reverse(10)
lis_reverse_500 = Sortirovki_pypy.list_reverse(500)
lis_reverse_1000 = Sortirovki_pypy.list_reverse(1_000)
lis_reverse_50000 = Sortirovki_pypy.list_reverse(50_000)
lis_reverse_1000000 = Sortirovki_pypy.list_reverse(1_000_000)

lis_almost_10 = Sortirovki_pypy.list_almost(10)
lis_almost_500 = Sortirovki_pypy.list_almost(500)
lis_almost_1000 = Sortirovki_pypy.list_almost(1_000)
lis_almost_50000 = Sortirovki_pypy.list_almost(50_000)
lis_almost_1000000 = Sortirovki_pypy.list_almost(1_000_000)


"""
print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_normal_10).bubble_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_normal_500).bubble_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_normal_1000).bubble_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_normal_50000).bubble_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_normal_1000000).bubble_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_random_10).bubble_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_random_500).bubble_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_random_1000).bubble_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_random_50000).bubble_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_random_1000000).bubble_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_reverse_10).bubble_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_reverse_500).bubble_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_reverse_1000).bubble_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_reverse_50000).bubble_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_reverse_1000000).bubble_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_almost_10).bubble_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_almost_500).bubble_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_almost_1000).bubble_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_almost_50000).bubble_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_almost_1000000).bubble_sort()}")"""




"""
print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_normal_10).insertion_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_normal_500).insertion_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_normal_1000).insertion_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_normal_50000).insertion_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_normal_1000000).insertion_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_random_10).insertion_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_random_500).insertion_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_random_1000).insertion_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_random_50000).insertion_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_random_1000000).insertion_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_reverse_10).insertion_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_reverse_500).insertion_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_reverse_1000).insertion_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_reverse_50000).insertion_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_reverse_1000000).insertion_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_almost_10).insertion_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_almost_500).insertion_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_almost_1000).insertion_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_almost_50000).insertion_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_almost_1000000).insertion_sort()}")

"""
"""

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_normal_10).selection_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_normal_500).selection_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_normal_1000).selection_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_normal_50000).selection_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_normal_1000000).selection_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_random_10).selection_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_random_500).selection_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_random_1000).selection_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_random_50000).selection_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_random_1000000).selection_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_reverse_10).selection_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_reverse_500).selection_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_reverse_1000).selection_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_reverse_50000).selection_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_reverse_1000000).selection_sort()}")

"""
print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_almost_10).selection_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_almost_500).selection_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_almost_1000).selection_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_almost_50000).selection_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_almost_1000000).selection_sort()}")



"""

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_normal_10).heap_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_normal_500).heap_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_normal_1000).heap_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_normal_50000).heap_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_normal_1000000).heap_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_random_10).heap_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_random_500).heap_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_random_1000).heap_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_random_50000).heap_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_random_1000000).heap_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_reverse_10).heap_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_reverse_500).heap_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_reverse_1000).heap_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_reverse_50000).heap_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_reverse_1000000).heap_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_almost_10).heap_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_almost_500).heap_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_almost_1000).heap_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_almost_50000).heap_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_almost_1000000).heap_sort()}")


  
"""
"""

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_normal_10).quick_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_normal_500).quick_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_normal_1000).quick_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_normal_50000).quick_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_normal_1000000).quick_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_random_10).quick_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_random_500).quick_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_random_1000).quick_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_random_50000).quick_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_random_1000000).quick_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_reverse_10).quick_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_reverse_500).quick_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_reverse_1000).quick_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_reverse_50000).quick_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_reverse_1000000).quick_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_almost_10).quick_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_almost_500).quick_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_almost_1000).quick_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_almost_50000).quick_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_almost_1000000).quick_sort()}")


"""
       


"""
print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_normal_10).merge_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_normal_500).merge_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_normal_1000).merge_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_normal_50000).merge_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_normal_1000000).merge_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_random_10).merge_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_random_500).merge_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_random_1000).merge_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_random_50000).merge_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_random_1000000).merge_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_reverse_10).merge_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_reverse_500).merge_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_reverse_1000).merge_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_reverse_50000).merge_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_reverse_1000000).merge_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_almost_10).merge_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_almost_500).merge_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_almost_1000).merge_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_almost_50000).merge_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_almost_1000000).merge_sort()}")

"""



"""
print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_normal_10).counting_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_normal_500).counting_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_normal_1000).counting_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_normal_50000).counting_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_normal_1000000).counting_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_random_10).counting_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_random_500).counting_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_random_1000).counting_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_random_50000).counting_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_random_1000000).counting_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_reverse_10).counting_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_reverse_500).counting_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_reverse_1000).counting_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_reverse_50000).counting_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_reverse_1000000).counting_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_almost_10).counting_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_almost_500).counting_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_almost_1000).counting_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_almost_50000).counting_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_almost_1000000).counting_sort()}")



"""
"""


print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_normal_10).radix_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_normal_500).radix_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_normal_1000).radix_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_normal_50000).radix_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_normal_1000000).radix_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_random_10).radix_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_random_500).radix_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_random_1000).radix_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_random_50000).radix_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_random_1000000).radix_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_reverse_10).radix_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_reverse_500).radix_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_reverse_1000).radix_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_reverse_50000).radix_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_reverse_1000000).radix_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_almost_10).radix_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_almost_500).radix_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_almost_1000).radix_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_almost_50000).radix_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_almost_1000000).radix_sort()}")
"""



"""

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_normal_10).bucket_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_normal_500).bucket_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_normal_1000).bucket_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_normal_50000).bucket_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_normal_1000000).bucket_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_random_10).bucket_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_random_500).bucket_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_random_1000).bucket_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_random_50000).bucket_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_random_1000000).bucket_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_reverse_10).bucket_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_reverse_500).bucket_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_reverse_1000).bucket_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_reverse_50000).bucket_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_reverse_1000000).bucket_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_almost_10).bucket_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_almost_500).bucket_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_almost_1000).bucket_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_almost_50000).bucket_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_almost_1000000).bucket_sort()}")

"""

"""


print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_normal_10).bubble_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_normal_500).bubble_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_normal_1000).bubble_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_normal_50000).bubble_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_normal_1000000).bubble_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_random_10).bubble_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_random_500).bubble_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_random_1000).bubble_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_random_50000).bubble_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_random_1000000).bubble_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_reverse_10).bubble_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_reverse_500).bubble_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_reverse_1000).bubble_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_reverse_50000).bubble_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_reverse_1000000).bubble_sort()}")

print( f"Время и память выполнения с 10 элементами: {Sortirovki_pypy(lis_almost_10).bubble_sort()}, \n",
       f"Время и память выполнения с 500 элементами: {Sortirovki_pypy(lis_almost_500).bubble_sort()}, \n",
       f"Время и память выполнения с 1000 элементов: {Sortirovki_pypy(lis_almost_1000).bubble_sort()}, \n", 
       f"Время и память выполнения с 50_000 элементов: {Sortirovki_pypy(lis_almost_50000).bubble_sort()}, \n",
       f"Время и память выполнения с 1_000_000 элементов: {Sortirovki_pypy(lis_almost_1000000).bubble_sort()}")
"""



