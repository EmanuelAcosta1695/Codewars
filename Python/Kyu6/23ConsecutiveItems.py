def get_length_of_missing_array(array_of_arrays: list):
    if array_of_arrays is None:
        return 0
    elif len(array_of_arrays) == 0:
        return 0
    for x in array_of_arrays:
        if x is None:
            return 0
        elif len(x) == 0:
            return 0
    array_of_arrays.sort(key=len)
    return [len(y)+1 for y, x in zip(array_of_arrays[:-1], array_of_arrays[1:]) if len(y) != len(x)-1 ][-1]

"""
You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!


You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

If the array of arrays is null/nil or empty, the method should return 0.

When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.
"""
