def count_red_beads(n):
    x = 0
    if n == 1:
        return 0
    else:
        for i in range(1,n):
            x = x + 2
        return x

"""
Description:
Two red beads are placed between every two blue beads. There are N blue beads. After looking at the arrangement below work out the number of red beads.

@ @@ @ @@ @ @@ @ @@ @ @@ @
"""
