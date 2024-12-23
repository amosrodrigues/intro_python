file = open("arquivo.txt", mode="w")

file.write("nome idade\n")
file.write("Maria 45\n")
file.write("Miguel 33\n")

print("Túlio 22", file=file)

LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
file.writelines(LINES)

file.close()

# arquivos = []
# for index in range(10240):
#     arquivos.append(open(f"arquivo{index}.txt", "w"))

file = open("arquivo.txt", mode="r")
content = file.read()
print(content)
file.close()

file = open("arquivo.txt", mode="r")
for line in file:
    print(line)
file.close()


file = open("arquivo-binario.dat", mode="wb")
file.write(b"C\xc3\xa1ssio 30")
file.close()

file = open("arquivo-binario.dat", mode="rb")
content = file.read()
print(content)
file.close()
