def odd_row(n):
    if n == 1: return [1]
    start = sum(x for x in range(n))
    stop = sum(x for x in range(n+1))
    range_start = sum([2*x for x in range(n)]) + 1
    return [range_start+x for x in range(0, 2*(stop-start), 2)]

"""
Given a triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

odd_row(1)  ==  [1]
odd_row(2)  ==  [3, 5]
odd_row(3)  ==  [7, 9, 11]
Note: your code should be optimized to handle big inputs.
"""
