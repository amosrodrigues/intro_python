# Cria o arquivo com os dados dos estudantes e suas notas
with open("arquivo.txt", mode="w") as file:
    file.write("Estudante Nota\n")
    file.write("Marcos 10\n")
    file.write("Felipe 4\n")
    file.write("José 6\n")
    file.write("Ana 10\n")
    file.write("Maria 9\n")
    file.write("Miguel 5\n")

# Lista para armazenar os estudantes em recuperação
recovery_students = []

# Lê o arquivo e filtra os estudantes com notas menores que 6
with open("arquivo.txt", mode="r") as grades_file:
    next(grades_file)  # Pula o cabeçalho
    for line in grades_file:
        student_grade = line.split()
        print(student_grade)
        if (
            len(student_grade) == 2
            and student_grade[1].isdigit()
            and int(student_grade[1]) < 6
        ):
            recovery_students.append(f"{student_grade[0]}\n")

# Escreve os estudantes em recuperação em um novo arquivo
with open("file.txt", mode="w") as new_file:
    for student in recovery_students:
        print(student.strip())  # Ao imprimir os nomes remove novas linhas extras
    new_file.writelines(recovery_students)
