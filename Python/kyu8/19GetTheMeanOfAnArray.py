import math

#2da mejor
def get_average(marks):
  return math.floor(sum(marks) / len(marks))


#1er solucion
def get_average(marks):
    count = len(marks)
    num = 0
    for i in marks:
        num += i
    return math.floor(num / count)


"""
It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.
"""
