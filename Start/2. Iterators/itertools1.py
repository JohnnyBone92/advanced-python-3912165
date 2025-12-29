# Example file for Advanced Python by Joe Marini
# Itertools: count, cycle, accumulate


import itertools

names = ["Joe", "Jane", "Jim"]

# cycle iterator can be used to cycle over a collection infinitely
# cycler = itertools.cycle(names)
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))

# use count to create a simple counter
# counter = itertools.count(start=100, step=10)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# accumulate creates an iterator that accumulates values
# vals = [10,20,30,40,50,40,30]
# acc = itertools.accumulate(vals, max)
# print(list(acc))

# amortize a loan over a set number of payments for a 2000 loan at 4%
# payments = [100, 125, 200, 105, 100, 120, 110, 130, 150, 100, 110, 120]
# update = lambda balance, payment: round(balance * 1.04) - payment
# balances = itertools.accumulate(payments, update, initial=2000)
# print(list(balances))

numbers = [
    [43, 2, 77, 48, 24, 9, 3, 65, 41, 42, 10, 75, 14, 69, 61],
    [20, 47, 69, 38, 2, 49, 76, 42, 81, 34, 10, 47, 76, 85, 81, 72],
    [92, 46, 25, 61, 75, 40, 87, 9, 52, 77, 0, 11, 25],
    [48, 74, 81, 71, 32, 82, 39, 74, 37, 72, 15],
    [8, 26, 12, 71, 5, 83, 75, 30, 34, 77]
]

def max_list(l, x):
    print(f'List: {l}, Element: {x}')
    return list(itertools.accumulate(x + l, max))

result = itertools.accumulate(numbers, max_list)
print(list(result)[-1][-1])