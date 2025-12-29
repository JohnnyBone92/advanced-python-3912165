# Example file for Advanced Python by Joe Marini


# define a list of days in English and French
import itertools


days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# the enumerate function
# for i, d in enumerate(days, start=1):
#     print(i, d)

# use zip to combine sequences
for d in zip(days, daysFr):
    print(d)

# use enumerate and zip together
for i, d in enumerate(zip(days, daysFr), start=1):
    print(i, d[0], "=", d[1], "in French")

# use zip_longest
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"
result = itertools.zip_longest(seq1, seq2, seq3, fillvalue="?")
for item in result:
    print(item)
    