from datetime import date

name = input("Kako se zoves?\n")

# print("zdravo: " + name)
print(f'zdravo: {name}')

dayOfBirthString = input("Datum rodjenja (YYYY-MM-DD)?\n")

dayOfBirth = date.fromisoformat(dayOfBirthString)

print(date.today() - dayOfBirth)
