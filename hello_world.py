''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def isEven(brojevi):
    return brojevi % 2


    
def partition(lista, func):
    both = []
    even = []
    odd = []
    for num in lista:
        x = func(num)
        if x == True:
            even.append(num)
        else:
            odd.append(num)
    both.append(even)
    both.append(odd)
    return both
