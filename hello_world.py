def chop(t):
    letters.remove("a")
    letters.remove("f")
    return None


letters = ["a", "b", "c", "d", "e", "f"]

print(chop(letters))


def middle(new_t):
    return new_t[1:-1]


print(middle(letters))
