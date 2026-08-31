from class_cpython import Sortirovki_cpython
import os
import pandas as pd

lis_normal_10 = Sortirovki_cpython.list_normal(10)
lis_normal_500 = Sortirovki_cpython.list_normal(500)
lis_normal_1000 = Sortirovki_cpython.list_normal(1_000)
lis_normal_50000 = Sortirovki_cpython.list_normal(50_000)
lis_normal_1000000 = Sortirovki_cpython.list_normal(1_000_000)

lis_random_10 = Sortirovki_cpython.list_random(10)
lis_random_500 = Sortirovki_cpython.list_random(500)
lis_random_1000 = Sortirovki_cpython.list_random(1_000)
lis_random_50000 = Sortirovki_cpython.list_random(50_000)
lis_random_1000000 = Sortirovki_cpython.list_random(1_000_000)

lis_reverse_10 = Sortirovki_cpython.list_reverse(10)
lis_reverse_500 = Sortirovki_cpython.list_reverse(500)
lis_reverse_1000 = Sortirovki_cpython.list_reverse(1_000)
lis_reverse_50000 = Sortirovki_cpython.list_reverse(50_000)
lis_reverse_1000000 = Sortirovki_cpython.list_reverse(1_000_000)

lis_almost_10 = Sortirovki_cpython.list_almost(10)
lis_almost_500 = Sortirovki_cpython.list_almost(500)
lis_almost_1000 = Sortirovki_cpython.list_almost(1_000)
lis_almost_50000 = Sortirovki_cpython.list_almost(50_000)
lis_almost_1000000 = Sortirovki_cpython.list_almost(1_000_000)

compilator = [ 
              'CPython', 'CPython', 'CPython', 'CPython', 'CPython', 'CPython', 'CPython', 'CPython', 'CPython'
             ]

algoritm = [
            'bubble', 'selection', 'insertion', 'quick', 'merge', 'heap', 'counting', 'radix', 'bucket'
           ]








n_10n = [
        Sortirovki_cpython(lis_normal_10).bubble_sort()[0],  Sortirovki_cpython(lis_normal_10).selection_sort()[0], Sortirovki_cpython(lis_normal_10).insertion_sort()[0],
        Sortirovki_cpython(lis_normal_10).quick_sort()[0], Sortirovki_cpython(lis_normal_10).merge_sort()[0], Sortirovki_cpython(lis_normal_10).heap_sort()[0],
        Sortirovki_cpython(lis_normal_10).counting_sort(), Sortirovki_cpython(lis_normal_10).radix_sort(), Sortirovki_cpython(lis_normal_10).bucket_sort()
        ]

n_10np = [
        Sortirovki_cpython(lis_normal_10).bubble_sort()[1],  Sortirovki_cpython(lis_normal_10).selection_sort()[1], Sortirovki_cpython(lis_normal_10).insertion_sort()[1],
        Sortirovki_cpython(lis_normal_10).quick_sort()[1], Sortirovki_cpython(lis_normal_10).merge_sort()[1], Sortirovki_cpython(lis_normal_10).heap_sort()[1],
        Sortirovki_cpython(lis_normal_10).counting_sort(), Sortirovki_cpython(lis_normal_10).radix_sort(), Sortirovki_cpython(lis_normal_10).bucket_sort()
        ]



n_500n = [
        Sortirovki_cpython(lis_normal_500).bubble_sort()[0],  Sortirovki_cpython(lis_normal_500).selection_sort()[0], Sortirovki_cpython(lis_normal_500).insertion_sort()[0],
        Sortirovki_cpython(lis_normal_500).quick_sort()[0], Sortirovki_cpython(lis_normal_500).merge_sort()[0], Sortirovki_cpython(lis_normal_500).heap_sort()[0],
        Sortirovki_cpython(lis_normal_500).counting_sort(), Sortirovki_cpython(lis_normal_500).radix_sort(), Sortirovki_cpython(lis_normal_500).bucket_sort()
        ]

n_500np = [
        Sortirovki_cpython(lis_normal_500).bubble_sort()[1],  Sortirovki_cpython(lis_normal_500).selection_sort()[1], Sortirovki_cpython(lis_normal_500).insertion_sort()[1],
        Sortirovki_cpython(lis_normal_500).quick_sort()[1], Sortirovki_cpython(lis_normal_500).merge_sort()[1], Sortirovki_cpython(lis_normal_500).heap_sort()[1],
        Sortirovki_cpython(lis_normal_500).counting_sort(), Sortirovki_cpython(lis_normal_500).radix_sort(), Sortirovki_cpython(lis_normal_500).bucket_sort()
        ]


n_1000n = [
        Sortirovki_cpython(lis_normal_1000).bubble_sort()[0],  Sortirovki_cpython(lis_normal_1000).selection_sort()[0], Sortirovki_cpython(lis_normal_1000).insertion_sort()[0],
        Sortirovki_cpython(lis_normal_1000).quick_sort()[0], Sortirovki_cpython(lis_normal_1000).merge_sort()[0], Sortirovki_cpython(lis_normal_1000).heap_sort()[0],
        Sortirovki_cpython(lis_normal_1000).counting_sort(), Sortirovki_cpython(lis_normal_1000).radix_sort(), Sortirovki_cpython(lis_normal_1000).bucket_sort()
         ]

n_1000np = [
        Sortirovki_cpython(lis_normal_1000).bubble_sort()[1],  Sortirovki_cpython(lis_normal_1000).selection_sort()[1], Sortirovki_cpython(lis_normal_1000).insertion_sort()[1],
        Sortirovki_cpython(lis_normal_1000).quick_sort()[1], Sortirovki_cpython(lis_normal_1000).merge_sort()[1], Sortirovki_cpython(lis_normal_1000).heap_sort()[1],
        Sortirovki_cpython(lis_normal_1000).counting_sort(), Sortirovki_cpython(lis_normal_1000).radix_sort(), Sortirovki_cpython(lis_normal_1000).bucket_sort()
        ]

n_50000n = [
        Sortirovki_cpython(lis_normal_10).bubble_sort()[0],  Sortirovki_cpython(lis_normal_10).selection_sort()[0], Sortirovki_cpython(lis_normal_10).insertion_sort()[0],
        Sortirovki_cpython(lis_normal_50000).quick_sort()[0], Sortirovki_cpython(lis_normal_50000).merge_sort()[0], Sortirovki_cpython(lis_normal_50000).heap_sort()[0],
        Sortirovki_cpython(lis_normal_50000).counting_sort()[0], Sortirovki_cpython(lis_normal_50000).radix_sort()[0], Sortirovki_cpython(lis_normal_50000).bucket_sort()[0]
          ]

n_50000np = [
        Sortirovki_cpython(lis_normal_10).bubble_sort()[1],  Sortirovki_cpython(lis_normal_10).selection_sort()[1], Sortirovki_cpython(lis_normal_10).insertion_sort()[1],
        Sortirovki_cpython(lis_normal_50000).quick_sort()[1], Sortirovki_cpython(lis_normal_50000).merge_sort()[1], Sortirovki_cpython(lis_normal_50000).heap_sort()[1],
        Sortirovki_cpython(lis_normal_50000).counting_sort()[1], Sortirovki_cpython(lis_normal_50000).radix_sort()[1], Sortirovki_cpython(lis_normal_50000).bucket_sort()[1]
        ]



n_1000000n = [
        Sortirovki_cpython(lis_normal_10).bubble_sort()[0],  Sortirovki_cpython(lis_normal_10).selection_sort()[0], Sortirovki_cpython(lis_normal_10).insertion_sort()[0],
        Sortirovki_cpython(lis_normal_10).quick_sort()[0], Sortirovki_cpython(lis_normal_10).merge_sort()[0], Sortirovki_cpython(lis_normal_10).heap_sort()[0],
        Sortirovki_cpython(lis_normal_1000000).counting_sort()[0], Sortirovki_cpython(lis_normal_1000000).radix_sort()[0], Sortirovki_cpython(lis_normal_1000000).bucket_sort()[0]
            ]

n_1000000np = [
        Sortirovki_cpython(lis_normal_10).bubble_sort()[1],  Sortirovki_cpython(lis_normal_10).selection_sort()[1], Sortirovki_cpython(lis_normal_10).insertion_sort()[1],
        Sortirovki_cpython(lis_normal_10).quick_sort()[1], Sortirovki_cpython(lis_normal_10).merge_sort()[1], Sortirovki_cpython(lis_normal_10).heap_sort()[1],
        Sortirovki_cpython(lis_normal_1000000).counting_sort()[1], Sortirovki_cpython(lis_normal_1000000).radix_sort()[1], Sortirovki_cpython(lis_normal_1000000).bucket_sort()[1]
        ]
            
            










n_10rev = [
        Sortirovki_cpython(lis_reverse_10).bubble_sort()[0],  Sortirovki_cpython(lis_reverse_10).selection_sort()[0], Sortirovki_cpython(lis_reverse_10).insertion_sort()[0],
        Sortirovki_cpython(lis_reverse_10).quick_sort()[0], Sortirovki_cpython(lis_reverse_10).merge_sort()[0], Sortirovki_cpython(lis_reverse_10).heap_sort()[0],
        Sortirovki_cpython(lis_reverse_10).counting_sort(), Sortirovki_cpython(lis_reverse_10).radix_sort(), Sortirovki_cpython(lis_reverse_10).bucket_sort()
       ]

n_10revp = [
        Sortirovki_cpython(lis_reverse_10).bubble_sort()[1],  Sortirovki_cpython(lis_reverse_10).selection_sort()[1], Sortirovki_cpython(lis_reverse_10).insertion_sort()[1],
        Sortirovki_cpython(lis_reverse_10).quick_sort()[1], Sortirovki_cpython(lis_reverse_10).merge_sort()[1], Sortirovki_cpython(lis_reverse_10).heap_sort()[1],
        Sortirovki_cpython(lis_reverse_10).counting_sort(), Sortirovki_cpython(lis_reverse_10).radix_sort(), Sortirovki_cpython(lis_reverse_10).bucket_sort()
       ]

n_500rev = [
        Sortirovki_cpython(lis_reverse_500).bubble_sort()[0],  Sortirovki_cpython(lis_reverse_500).selection_sort()[0], Sortirovki_cpython(lis_reverse_500).insertion_sort()[0],
        Sortirovki_cpython(lis_reverse_500).quick_sort()[0], Sortirovki_cpython(lis_reverse_500).merge_sort()[0], Sortirovki_cpython(lis_reverse_500).heap_sort()[0],
        Sortirovki_cpython(lis_reverse_500).counting_sort(), Sortirovki_cpython(lis_reverse_500).radix_sort(), Sortirovki_cpython(lis_reverse_500).bucket_sort()
        ]

n_500revp = [
        Sortirovki_cpython(lis_reverse_500).bubble_sort()[1],  Sortirovki_cpython(lis_reverse_500).selection_sort()[1], Sortirovki_cpython(lis_reverse_500).insertion_sort()[1],
        Sortirovki_cpython(lis_reverse_500).quick_sort()[1], Sortirovki_cpython(lis_reverse_500).merge_sort()[1], Sortirovki_cpython(lis_reverse_500).heap_sort()[1],
        Sortirovki_cpython(lis_reverse_500).counting_sort(), Sortirovki_cpython(lis_reverse_500).radix_sort(), Sortirovki_cpython(lis_reverse_500).bucket_sort()
       ]


n_1000rev = [
        Sortirovki_cpython(lis_reverse_1000).bubble_sort()[0],  Sortirovki_cpython(lis_reverse_1000).selection_sort()[0], Sortirovki_cpython(lis_reverse_1000).insertion_sort()[0],
        Sortirovki_cpython(lis_reverse_1000).quick_sort()[0], Sortirovki_cpython(lis_reverse_1000).merge_sort()[0], Sortirovki_cpython(lis_reverse_1000).heap_sort()[0],
        Sortirovki_cpython(lis_reverse_1000).counting_sort(), Sortirovki_cpython(lis_reverse_1000).radix_sort(), Sortirovki_cpython(lis_reverse_1000).bucket_sort()
         ]

n_1000revp = [
        Sortirovki_cpython(lis_reverse_1000).bubble_sort()[1],  Sortirovki_cpython(lis_reverse_1000).selection_sort()[1], Sortirovki_cpython(lis_reverse_1000).insertion_sort()[1],
        Sortirovki_cpython(lis_reverse_1000).quick_sort()[1], Sortirovki_cpython(lis_reverse_1000).merge_sort()[1], Sortirovki_cpython(lis_reverse_1000).heap_sort()[1],
        Sortirovki_cpython(lis_reverse_1000).counting_sort(), Sortirovki_cpython(lis_reverse_1000).radix_sort(), Sortirovki_cpython(lis_reverse_1000).bucket_sort()
       ]

n_50000rev = [
        Sortirovki_cpython(lis_reverse_10).bubble_sort()[0],  Sortirovki_cpython(lis_reverse_10).selection_sort()[0], Sortirovki_cpython(lis_reverse_10).insertion_sort()[0],
        Sortirovki_cpython(lis_reverse_50000).quick_sort()[0], Sortirovki_cpython(lis_reverse_50000).merge_sort()[0], Sortirovki_cpython(lis_reverse_50000).heap_sort()[0],
        Sortirovki_cpython(lis_reverse_50000).counting_sort()[0], Sortirovki_cpython(lis_reverse_50000).radix_sort()[0], Sortirovki_cpython(lis_reverse_50000).bucket_sort()[0]
          ]

n_50000revp = [
        Sortirovki_cpython(lis_reverse_10).bubble_sort()[1],  Sortirovki_cpython(lis_reverse_10).selection_sort()[1], Sortirovki_cpython(lis_reverse_10).insertion_sort()[1],
        Sortirovki_cpython(lis_reverse_50000).quick_sort()[1], Sortirovki_cpython(lis_reverse_50000).merge_sort()[1], Sortirovki_cpython(lis_reverse_50000).heap_sort()[1],
        Sortirovki_cpython(lis_reverse_50000).counting_sort()[1], Sortirovki_cpython(lis_reverse_50000).radix_sort()[1], Sortirovki_cpython(lis_reverse_50000).bucket_sort()[1]
       ]


n_1000000rev = [
        Sortirovki_cpython(lis_reverse_10).bubble_sort()[0],  Sortirovki_cpython(lis_reverse_10).selection_sort()[0], Sortirovki_cpython(lis_reverse_10).insertion_sort()[0],
        Sortirovki_cpython(lis_reverse_10).quick_sort()[0], Sortirovki_cpython(lis_reverse_10).merge_sort()[0], Sortirovki_cpython(lis_reverse_10).heap_sort()[0],
        Sortirovki_cpython(lis_reverse_1000000).counting_sort()[0], Sortirovki_cpython(lis_reverse_1000000).radix_sort()[0], Sortirovki_cpython(lis_reverse_1000000).bucket_sort()[0]
            ]

n_1000000revp = [
        Sortirovki_cpython(lis_reverse_10).bubble_sort()[1],  Sortirovki_cpython(lis_reverse_10).selection_sort()[1], Sortirovki_cpython(lis_reverse_10).insertion_sort()[1],
        Sortirovki_cpython(lis_reverse_10).quick_sort()[1], Sortirovki_cpython(lis_reverse_10).merge_sort()[1], Sortirovki_cpython(lis_reverse_10).heap_sort()[1],
        Sortirovki_cpython(lis_reverse_1000000).counting_sort()[1], Sortirovki_cpython(lis_reverse_1000000).radix_sort()[1], Sortirovki_cpython(lis_reverse_1000000).bucket_sort()[1]
       ]            













n_10ran = [
        Sortirovki_cpython(lis_random_10).bubble_sort()[0],  Sortirovki_cpython(lis_random_10).selection_sort()[0], Sortirovki_cpython(lis_random_10).insertion_sort()[0],
        Sortirovki_cpython(lis_random_10).quick_sort()[0], Sortirovki_cpython(lis_random_10).merge_sort()[0], Sortirovki_cpython(lis_random_10).heap_sort()[0],
        Sortirovki_cpython(lis_random_10).counting_sort(), Sortirovki_cpython(lis_random_10).radix_sort(), Sortirovki_cpython(lis_random_10).bucket_sort()
       ]

n_10ranp = [
        Sortirovki_cpython(lis_random_10).bubble_sort()[1],  Sortirovki_cpython(lis_random_10).selection_sort()[1], Sortirovki_cpython(lis_random_10).insertion_sort()[1],
        Sortirovki_cpython(lis_random_10).quick_sort()[1], Sortirovki_cpython(lis_random_10).merge_sort()[1], Sortirovki_cpython(lis_random_10).heap_sort()[1],
        Sortirovki_cpython(lis_random_10).counting_sort(), Sortirovki_cpython(lis_random_10).radix_sort(), Sortirovki_cpython(lis_random_10).bucket_sort()
       ]

n_500ran = [
        Sortirovki_cpython(lis_random_500).bubble_sort()[0],  Sortirovki_cpython(lis_random_500).selection_sort()[0], Sortirovki_cpython(lis_random_500).insertion_sort()[0],
        Sortirovki_cpython(lis_random_500).quick_sort()[0], Sortirovki_cpython(lis_random_500).merge_sort()[0], Sortirovki_cpython(lis_random_500).heap_sort()[0],
        Sortirovki_cpython(lis_random_500).counting_sort(), Sortirovki_cpython(lis_random_500).radix_sort(), Sortirovki_cpython(lis_random_500).bucket_sort()
        ]

n_500ranp = [
        Sortirovki_cpython(lis_random_500).bubble_sort()[1],  Sortirovki_cpython(lis_random_500).selection_sort()[1], Sortirovki_cpython(lis_random_500).insertion_sort()[1],
        Sortirovki_cpython(lis_random_500).quick_sort()[1], Sortirovki_cpython(lis_random_500).merge_sort()[1], Sortirovki_cpython(lis_random_500).heap_sort()[1],
        Sortirovki_cpython(lis_random_500).counting_sort(), Sortirovki_cpython(lis_random_500).radix_sort(), Sortirovki_cpython(lis_random_500).bucket_sort()
        ]

n_1000ran = [
        Sortirovki_cpython(lis_random_1000).bubble_sort()[0],  Sortirovki_cpython(lis_random_1000).selection_sort()[0], Sortirovki_cpython(lis_random_1000).insertion_sort()[0],
        Sortirovki_cpython(lis_random_1000).quick_sort()[0], Sortirovki_cpython(lis_random_1000).merge_sort()[0], Sortirovki_cpython(lis_random_1000).heap_sort()[0],
        Sortirovki_cpython(lis_random_1000).counting_sort(), Sortirovki_cpython(lis_random_1000).radix_sort(), Sortirovki_cpython(lis_random_1000).bucket_sort()
         ]

n_1000ranp = [
        Sortirovki_cpython(lis_random_1000).bubble_sort()[1],  Sortirovki_cpython(lis_random_1000).selection_sort()[1], Sortirovki_cpython(lis_random_1000).insertion_sort()[1],
        Sortirovki_cpython(lis_random_1000).quick_sort()[1], Sortirovki_cpython(lis_random_1000).merge_sort()[1], Sortirovki_cpython(lis_random_1000).heap_sort()[1],
        Sortirovki_cpython(lis_random_1000).counting_sort(), Sortirovki_cpython(lis_random_1000).radix_sort(), Sortirovki_cpython(lis_random_1000).bucket_sort()
         ]

n_50000ran = [
        Sortirovki_cpython(lis_random_10).bubble_sort()[0],  Sortirovki_cpython(lis_random_10).selection_sort()[0], Sortirovki_cpython(lis_random_10).insertion_sort()[0],
        Sortirovki_cpython(lis_random_50000).quick_sort()[0], Sortirovki_cpython(lis_random_50000).merge_sort()[0], Sortirovki_cpython(lis_random_50000).heap_sort()[0],
        Sortirovki_cpython(lis_random_50000).counting_sort()[0], Sortirovki_cpython(lis_random_50000).radix_sort()[0], Sortirovki_cpython(lis_random_50000).bucket_sort()[0]
          ]

n_50000ranp = [
        Sortirovki_cpython(lis_random_10).bubble_sort()[1],  Sortirovki_cpython(lis_random_10).selection_sort()[1], Sortirovki_cpython(lis_random_10).insertion_sort()[1],
        Sortirovki_cpython(lis_random_50000).quick_sort()[1], Sortirovki_cpython(lis_random_50000).merge_sort()[1], Sortirovki_cpython(lis_random_50000).heap_sort()[1],
        Sortirovki_cpython(lis_random_50000).counting_sort()[1], Sortirovki_cpython(lis_random_50000).radix_sort()[1], Sortirovki_cpython(lis_random_50000).bucket_sort()[1]
          ]



n_1000000ran = [
        Sortirovki_cpython(lis_random_10).bubble_sort()[0],  Sortirovki_cpython(lis_random_10).selection_sort()[0], Sortirovki_cpython(lis_random_10).insertion_sort()[0],
        Sortirovki_cpython(lis_random_10).quick_sort()[0], Sortirovki_cpython(lis_random_10).merge_sort()[0], Sortirovki_cpython(lis_random_10).heap_sort()[0],
        Sortirovki_cpython(lis_random_1000000).counting_sort()[0], Sortirovki_cpython(lis_random_1000000).radix_sort()[0], Sortirovki_cpython(lis_random_1000000).bucket_sort()[0]
            ]

n_1000000ranp = [
        Sortirovki_cpython(lis_random_10).bubble_sort()[1],  Sortirovki_cpython(lis_random_10).selection_sort()[1], Sortirovki_cpython(lis_random_10).insertion_sort()[1],
        Sortirovki_cpython(lis_random_10).quick_sort()[1], Sortirovki_cpython(lis_random_10).merge_sort()[1], Sortirovki_cpython(lis_random_10).heap_sort()[1],
        Sortirovki_cpython(lis_random_1000000).counting_sort()[1], Sortirovki_cpython(lis_random_1000000).radix_sort()[1], Sortirovki_cpython(lis_random_1000000).bucket_sort()[1]
            ]

















n_10a = [
        Sortirovki_cpython(lis_almost_10).bubble_sort()[0],  Sortirovki_cpython(lis_almost_10).selection_sort()[0], Sortirovki_cpython(lis_almost_10).insertion_sort()[0],
        Sortirovki_cpython(lis_almost_10).quick_sort()[0], Sortirovki_cpython(lis_almost_10).merge_sort()[0], Sortirovki_cpython(lis_almost_10).heap_sort()[0],
        Sortirovki_cpython(lis_almost_10).counting_sort(), Sortirovki_cpython(lis_almost_10).radix_sort(), Sortirovki_cpython(lis_almost_10).bucket_sort()
       ]

n_10ap = [
        Sortirovki_cpython(lis_almost_10).bubble_sort()[1],  Sortirovki_cpython(lis_almost_10).selection_sort()[1], Sortirovki_cpython(lis_almost_10).insertion_sort()[1],
        Sortirovki_cpython(lis_almost_10).quick_sort()[1], Sortirovki_cpython(lis_almost_10).merge_sort()[1], Sortirovki_cpython(lis_almost_10).heap_sort()[1],
        Sortirovki_cpython(lis_almost_10).counting_sort(), Sortirovki_cpython(lis_almost_10).radix_sort(), Sortirovki_cpython(lis_almost_10).bucket_sort()
       ]

n_500a = [
        Sortirovki_cpython(lis_almost_500).bubble_sort()[0],  Sortirovki_cpython(lis_almost_500).selection_sort()[0], Sortirovki_cpython(lis_almost_500).insertion_sort()[0],
        Sortirovki_cpython(lis_almost_500).quick_sort()[0], Sortirovki_cpython(lis_almost_500).merge_sort()[0], Sortirovki_cpython(lis_almost_500).heap_sort()[0],
        Sortirovki_cpython(lis_almost_500).counting_sort(), Sortirovki_cpython(lis_almost_500).radix_sort(), Sortirovki_cpython(lis_almost_500).bucket_sort()
        ]

n_500ap = [
        Sortirovki_cpython(lis_almost_500).bubble_sort()[1],  Sortirovki_cpython(lis_almost_500).selection_sort()[1], Sortirovki_cpython(lis_almost_500).insertion_sort()[1],
        Sortirovki_cpython(lis_almost_500).quick_sort()[1], Sortirovki_cpython(lis_almost_500).merge_sort()[1], Sortirovki_cpython(lis_almost_500).heap_sort()[1],
        Sortirovki_cpython(lis_almost_500).counting_sort(), Sortirovki_cpython(lis_almost_500).radix_sort(), Sortirovki_cpython(lis_almost_500).bucket_sort()
        ]

n_1000a = [
        Sortirovki_cpython(lis_almost_1000).bubble_sort()[0],  Sortirovki_cpython(lis_almost_1000).selection_sort()[0], Sortirovki_cpython(lis_almost_1000).insertion_sort()[0],
        Sortirovki_cpython(lis_almost_1000).quick_sort()[0], Sortirovki_cpython(lis_almost_1000).merge_sort()[0], Sortirovki_cpython(lis_almost_1000).heap_sort()[0],
        Sortirovki_cpython(lis_almost_1000).counting_sort(), Sortirovki_cpython(lis_almost_1000).radix_sort(), Sortirovki_cpython(lis_almost_1000).bucket_sort()
         ]

n_1000ap = [
        Sortirovki_cpython(lis_almost_1000).bubble_sort()[1],  Sortirovki_cpython(lis_almost_1000).selection_sort()[1], Sortirovki_cpython(lis_almost_1000).insertion_sort()[1],
        Sortirovki_cpython(lis_almost_1000).quick_sort()[1], Sortirovki_cpython(lis_almost_1000).merge_sort()[1], Sortirovki_cpython(lis_almost_1000).heap_sort()[1],
        Sortirovki_cpython(lis_almost_1000).counting_sort(), Sortirovki_cpython(lis_almost_1000).radix_sort(), Sortirovki_cpython(lis_almost_1000).bucket_sort()
         ]

n_50000a = [
        Sortirovki_cpython(lis_almost_10).bubble_sort()[0],  Sortirovki_cpython(lis_almost_10).selection_sort()[0], Sortirovki_cpython(lis_almost_10).insertion_sort()[0],
        Sortirovki_cpython(lis_almost_50000).quick_sort()[0], Sortirovki_cpython(lis_almost_50000).merge_sort()[0], Sortirovki_cpython(lis_almost_50000).heap_sort()[0],
        Sortirovki_cpython(lis_almost_50000).counting_sort()[0], Sortirovki_cpython(lis_almost_50000).radix_sort()[0], Sortirovki_cpython(lis_almost_50000).bucket_sort()[0]
          ]

n_50000ap = [
        Sortirovki_cpython(lis_almost_10).bubble_sort()[1],  Sortirovki_cpython(lis_almost_10).selection_sort()[1], Sortirovki_cpython(lis_almost_10).insertion_sort()[1],
        Sortirovki_cpython(lis_almost_50000).quick_sort()[1], Sortirovki_cpython(lis_almost_50000).merge_sort()[1], Sortirovki_cpython(lis_almost_50000).heap_sort()[1],
        Sortirovki_cpython(lis_almost_50000).counting_sort()[1], Sortirovki_cpython(lis_almost_50000).radix_sort()[1], Sortirovki_cpython(lis_almost_50000).bucket_sort()[1]
          ]


n_1000000a = [
        Sortirovki_cpython(lis_almost_10).bubble_sort()[0],  Sortirovki_cpython(lis_almost_10).selection_sort()[0], Sortirovki_cpython(lis_almost_10).insertion_sort()[0],
        Sortirovki_cpython(lis_almost_10).quick_sort()[0], Sortirovki_cpython(lis_almost_10).merge_sort()[0], Sortirovki_cpython(lis_almost_10).heap_sort()[0],
        Sortirovki_cpython(lis_almost_1000000).counting_sort(), Sortirovki_cpython(lis_almost_1000000).radix_sort(), Sortirovki_cpython(lis_almost_1000000).bucket_sort()
            ]

n_1000000ap = [
        Sortirovki_cpython(lis_almost_10).bubble_sort()[1],  Sortirovki_cpython(lis_almost_10).selection_sort()[1], Sortirovki_cpython(lis_almost_10).insertion_sort()[1],
        Sortirovki_cpython(lis_almost_10).quick_sort()[1], Sortirovki_cpython(lis_almost_10).merge_sort()[1], Sortirovki_cpython(lis_almost_10).heap_sort()[1],
        Sortirovki_cpython(lis_almost_1000000).counting_sort()[1], Sortirovki_cpython(lis_almost_1000000).radix_sort()[1], Sortirovki_cpython(lis_almost_1000000).bucket_sort()[1]
            ]





df_1 = pd.DataFrame({"Компилятор": compilator, " Алгоритм": algoritm, "N10-мс": n_10n, "N10-кб": n_10np, "N500-мc": n_500n, "N500-кб": n_500np, "N1000-мc": n_1000n, "N1000-кб": n_1000np, "N50000-мc": n_50000n,  "N50000-кб": n_50000np, "N1000000-мc": n_1000000n,  "N1000000-кб": n_1000000np})
df_1.to_csv("var_normal_pypy.csv", index=False,  mode="a", sep=",", header=not os.path.isfile("var_normal_pypy.csv"))


df_2 = pd.DataFrame({"Компилятор": compilator, " Алгоритм": algoritm, "N10-мc": n_10rev, "N10-кб": n_10revp, "N500-мc": n_500rev, "N500-кб": n_500revp, "N1000-мc": n_1000rev, "N1000-кб": n_1000revp,  "N50000-мc": n_50000rev,  "N50000-кб": n_50000revp, "N1000000-мc": n_1000000rev,  "N1000000-кб": n_1000000revp})
df_2.to_csv("var_reverse_pypy.csv", index=False,  mode="a", sep=",", header=not os.path.isfile("var_reverse_pypy.csv"))


df_3 = pd.DataFrame({"Компилятор": compilator, " Алгоритм": algoritm, "N10-мc": n_10ran, "N10-кб": n_10ranp, "N500-мc": n_500ran, "N500-кб": n_500ranp, "N1000-мc": n_1000ran, "N1000-кб": n_1000ranp, "N50000-мc": n_50000ran,  "N50000-кб": n_50000ranp,  "N1000000-мc": n_1000000ran,  "N1000000-кб": n_1000000ranp})
df_3.to_csv("var_random_pypy.csv", index=False,  mode="a", sep=",", header=not os.path.isfile("var_random_pypy.csv"))


df_4 = pd.DataFrame({"Компилятор": compilator, " Алгоритм": algoritm, "N10-мc": n_10a, "N10-кб": n_10ap, "N500-мc": n_500a, "N500-кб": n_500ap, "N1000-мc": n_1000a, "N1000-кб": n_1000ap, "N50000-мc": n_50000a,  "N50000-кб": n_50000ap,  "N1000000-мc": n_1000000a,  "N1000000-кб": n_1000000ap})
df_4.to_csv("var_almost_pypy.csv", index=False,  mode="a", sep=",", header=not os.path.isfile("var_almost_pypy.csv"))

