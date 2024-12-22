# position, salary = "", 2000
# if salary <= 2000:
#     position = "estagiário"
# elif 2000 < salary <= 5800:
#     position = "júnior"
# elif 5800 < salary <= 7500:
#     position = "pleno"
# elif 7500 < salary <= 10500:
#     position = "senior"
# else:
#     position = "líder"

# print(position)

# restaurants = [
#     {"name": "Restaurante A", "nota": 4.5},
#     {"name": "Restaurante B", "nota": 3.0},
#     {"name": "Restaurante C", "nota": 4.2},
#     {"name": "restaurante D", "nota": 2.3},
# ]

# filtered_restaurants = []
# min_rating = 3.0
# for restaurant in restaurants:
#     if restaurant["nota"] > min_rating:
#         filtered_restaurants.append(restaurant)

# filtered_restaurants = [
#     restaurant["name"] for restaurant in restaurants if restaurant["nota"] > min_rating
# ]

# print(filtered_restaurants)

# for index in range(6):
#     print(index)

# n = 10
# last, next = 0, 1
# while last < n:
#     print(last)
#     last, next = next, last + next

# languages = ["Python", "Java", "JavaScript"]

# enumerate_prime = enumerate(languages)

# print(list(enumerate_prime))

# for index, language in enumerate(list(languages)):
#     print(f"{index} - {language}")

# number = 5
# counter = 1
# result = 1

# while counter <= number:
#     result *= counter
#     counter += 1
#     print(result)
# result

# number, result = 5, 1

# for factor in range(1, number + 1):
#     result *= factor
#     print(result)
# result

# ratings = [6, 8, 5, 9, 10]
# new_ratings = []

# for rating in ratings:
#     new_ratings.append(rating * 10)
# new_ratings = [10 * rating for rating in ratings]
# print(new_ratings)

# for rating in ratings:
#     if (rating % 3) == 0:
#         print(f"{rating} é múltiplo de 3")

# restul = [print(f"{rating} é múltiplo de 3") for rating in ratings if (rating % 3) == 0]


# def soma(x, y):
#     return x * y


# print(soma(2, 2))

# print(soma(x=3, y=3))


# def concat_like_tuple(*args):
#     final_string = ""
#     for index, name in enumerate(args, 1):
#         final_string += f"O nome da pessoa {index} é {name}. \n"
#     return final_string


# def concat_like_dict(**kwargs):
#     final_string = (
#         f'{kwargs["nome"]} {kwargs["sobrenome"]} tem {kwargs["idade"]} anos. \n'
#     )
#     return final_string


# print(concat_like_tuple("Cris", "Wallace", "Carol"))

# print(concat_like_dict(nome="Felipe", sobrenome="Silva", idade=25))
