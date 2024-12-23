NAME = input("Digite seu nome: ")

for index, letter in enumerate(NAME, 1):
    print(f"{index}ª - {letter.upper()}")
