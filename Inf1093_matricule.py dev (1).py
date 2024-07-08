# Collection de nombres
numbers = []
nb = int(input("Combien de nombres : "))

for i in range(nb):
    nombre = int(input(f"Nombre {i+1}: "))
    numbers.append(nombre)

# Affichage des nombres
print("Les nombres saisis sont : ", numbers)

# Lire la valeur à rechercher
search_nb = int(input("Quel nombre à chercher ? "))

# Recherche séquentielle
position = -1
for i in range(len(numbers)):
    if search_nb == numbers[i]:
        position = i
        break

if position > -1:
    print(f"{search_nb} est à la position {position}")
else:
    print(f"{search_nb} n'existe pas dans le tableau")

# Recherche dichotomique lorsque le tableau est trié
numbers.sort()
print("Tableau trié pour la recherche dichotomique : ", numbers)

found = False
begin = 0
end = len(numbers) - 1
while not found and begin <= end:
    mid = (begin + end) // 2
    if search_nb == numbers[mid]:
        found = True
        print("Nombre trouvé à la position : ", mid)
    else:
        if search_nb < numbers[mid]:
            end = mid - 1
        else:
            begin = mid + 1

if not found:
    print("Nombre inexistant")
