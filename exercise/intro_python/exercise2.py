# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def mean_other(numbers):
    return sum(numbers) / len(numbers)


print(mean([1, 3, 5]))
