def interleave(string1, string2):
    string1 = tuple(string1)
    string2 = tuple(string2)
    string3 = list(zip(string1, string2))
    x = ["".join(x) for x in string3]
    return "".join(x)


print(interleave("hi","ha"))
