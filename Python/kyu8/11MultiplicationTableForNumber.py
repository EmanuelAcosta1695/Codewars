def multi_table(number):
    return "".join("1 * " + str(number) + " = " +  str(1 * number) + "\n" + "2 * " + str(number) + " = " +  str(2 * number) + "\n" + "3 * " + str(number) + " = " +  str(3 * number) + "\n" + "4 * " + str(number) + " = " +  str(4 * number) + "\n"  + "5 * " + str(number) + " = " +  str(5 * number) + "\n" + "6 * " + str(number) + " = " +  str(6 * number) + "\n" + "7 * " + str(number) + " = " +  str(7 * number) + "\n" + "8 * " + str(number) + " = " +  str(8 * number) + "\n" + "9 * " + str(number) + " = " +  str(9 * number) + "\n" + "10 * " + str(number) + " = " +  str(10 * number) + "\n") 
  
print(multi_table(7))

"""
Your goal is to return multiplication table for number that is always an integer from 1 to 10.

For example, a multiplication table (string) for number == 5 looks like below:

1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
P. S. You can use \n in string to jump to the next line.

Note: newlines should be added between rows, but there should be no trailing newline at the end.
"""