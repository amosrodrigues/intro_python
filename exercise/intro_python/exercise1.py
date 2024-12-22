# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def return_max(num_1, num_2):
    return max(num_1, num_2)


def bigger(number, other):
    if other > number:
        return other
    return number


print(return_max(2, 3))
