from random import choice

def make_laugh_func(person):
    def get_laugh():
        laugh = choice(("HAHAHAHHA", "lol", "teheheh"))
        return f"{laugh} {person}"
    return get_laugh

laugh_at = make_laugh_func("Linda")
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())


