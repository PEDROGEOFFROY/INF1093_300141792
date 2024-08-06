
# Question 1
listIdName = [
    (202401, "Anani"), (202402, "Simon"), (202403, "Pierre"), (202404, "Kylian"),
    (202405, "Alphonse"), (202406, "Joshua"), (202407, "Colince"), (202408, "Khristian"),
    (202409, "Zinedine"), (202410, "Didier")
]
print(listIdName)

# Exercice 2
# Question 1
def searchNameById(name):
    for id, n in listIdName:
        if n == name:
            return id
    return 0

print("Le matricule de Anani : ", searchNameById("Anani"))  # Le matricule de Anani :  202401 
print("Le matricule de Peter : ", searchNameById("Peter"))  # Le matricule de Peter :  0

# Question 2
listIdGrade = [
    (202401, 85), (202402, 90), (202403, 73), (202404, 88),
    (202405, 76), (202406, 82), (202407, 94), (202408, 78),
    (202409, 91), (202410, ,80)
]

def searchGradeByIdSeq(id):
    for i, grade in listIdGrade:
        if i == id:
            return grade
    return 0

print("La note Matricule 202403 est : ", searchGradeByIdSeq(202403))  # La note du matricule 202403 est de  :  73
print("La note Matricule 202405 est : ", searchGradeByIdSeq(202405))  # La note du matricule 202405 est de  :  76

# Question 3
def buildListSeq():
    return listIdGrade

fullList = buildListSeq()
print(fullList)  # Affiche la liste complète des notes

# Exercice 3
# Question 1: implémentons le tri de ton choix
def tri(lst):
    return sorted(lst, key=lambda x: x[1])  # Trie par la valeur (note)

listIdGrade = tri(listIdGrade)
print(listIdGrade)

# Question 2
def searchGradeByIdDicho(id):
    # La liste doit être triée pour la recherche dichotomique
    sortedList = sorted(listIdGrade)
    cout, long = 0, len(sortedList) - 1
    while cout <= long:
        milieu = (cout + long) // 2
        if sortedList[milieu][0] == id:
            return sortedList[milieu][1]
        elif sortedList[milieu][0] < id:
            cout = milieu + 1
        else:
            long = milieu - 1
    return 0

print("La note du matricule 202403 est de  : ", searchGradeByIdDicho(202403))
print("La note du matricule 202405 est de  : ", searchGradeByIdDicho(202405))

# Question 3
def buildListDicho():
    return sorted(listIdGrade)

fullListDicho = buildListDicho()
print(fullListDicho)

# dicotomique parce qu'elle est un algorithme puissant qui permet de faire des calcul
