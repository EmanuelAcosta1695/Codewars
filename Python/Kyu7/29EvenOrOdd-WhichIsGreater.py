def even_or_odd(s):
    z = 0
    b = 0
    for x in s[::1]:
        if x.isdigit():
            if int(x)%2 == 0:
                z = z + int(x)
            else:
                b = b + int(x)
    if z>b:
        return 'Even is greater than Odd'
    elif b>z:
        return 'Odd is greater than Even'
    elif z==b:
        return 'Even and Odd are the same'

"""
Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.

If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"

If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"

If the total of both even and odd numbers are identical return: "Even and Odd are the same"
"""
