def get_unlimited_multiples(number=1):
  sum = number
  while True:
    yield sum
    sum += number



sevens = get_unlimited_multiples(7)
[print(next(sevens)) for i in range(15)]
