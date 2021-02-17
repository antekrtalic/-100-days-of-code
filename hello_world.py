def triple_and_filter(arry):
    x = [x*3 for x in arry if x % 4 == 0]
    return x

print(triple_and_filter([1,2,3,4]))
