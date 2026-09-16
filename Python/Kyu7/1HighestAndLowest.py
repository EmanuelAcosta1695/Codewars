def high_and_low(numbers):
    numbers = numbers.split(' ')
    numbers = sorted(numbers, key=int)
    return numbers[-1] + ' ' + numbers[0]

"""ejercicio
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

"""
