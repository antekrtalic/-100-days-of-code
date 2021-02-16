def sum_floats(*fls):
    return sum(fl for fl in fls if type(fl) == float)

print(sum_floats(1.5, 2.4, 'awesome', [], 1))
