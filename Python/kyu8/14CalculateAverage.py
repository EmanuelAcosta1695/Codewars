def find_average(numbers):
    return sum(numbers) / len(numbers)

"""
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.

primera solucuion PERO NO COMPLETA: tiraba error en los problemas con muchos decimales. habia un tipo q no sabia cmo definirlo

def find_average(numbers):
    count = 0
    for x in numbers:
        count += 1
        if numbers == [0]:
            count += 1
    
    for y in numbers:
        y += x

    return round(float(y/count))
"""

