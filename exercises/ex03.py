print("Make a function that receive age, and return what they drink.")

# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.

# Rules:

# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.

idade = int(input("How old?"))
def people_with_age_drink(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'

print(people_with_age_drink(idade))