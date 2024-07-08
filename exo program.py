import os

# Fonction pour lister les fichiers dans un répertoire
def listing_directory(directory):
    files = []
    # Parcourir tous les éléments dans le répertoire
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        # Vérifier si l'élément est un fichier
        if os.path.isfile(item_path):
            # Séparer le nom du fichier et son extension
            file_name, ext = os.path.splitext(item)
            # Obtenir la taille du fichier en Mo
            size = os.path.getsize(item_path) / (1024 * 1024)
            # Ajouter le triplet (nom, extension, taille) à la liste
            files.append((file_name, ext, size))
    return files

# Fonction de tri par sélection basé sur la taille du fichier
def selection_sort(files):
    n = len(files)
    # Parcourir chaque élément de la liste
    for i in range(n):
        min_idx = i
        # Trouver l'élément le plus petit dans la liste non triée
        for j in range(i+1, n):
            if files[j][2] < files[min_idx][2]:
                min_idx = j
        # Échanger l'élément trouvé avec le premier élément
        files[i], files[min_idx] = files[min_idx], files[i]
    return files

# Fonction de tri à bulles basé sur le nom du fichier
def bubble_sort(files):
    n = len(files)
    # Parcourir chaque élément de la liste
    for i in range(n):
        # Parcourir la liste de 0 à n-i-1
        for j in range(0, n-i-1):
            # Échanger si l'élément trouvé est plus grand que le suivant
            if files[j][0] > files[j+1][0]:
                files[j], files[j+1] = files[j+1], files[j]
    return files

# Exemple d'utilisation
if __name__ == "__main__":
    # Définir le chemin du répertoire à analyser
    directory_path = "/chemin/vers/le/repertoire"

    # Lister les fichiers dans le répertoire
    files_list = listing_directory(directory_path)
    print("Fichiers listés :", files_list)

    # Trier les fichiers par taille
    sorted_files_by_size = selection_sort(files_list.copy())
    print("Fichiers triés par taille :", sorted_files_by_size)

    # Trier les fichiers par nom
    sorted_files_by_name = bubble_sort(files_list.copy())
    print("Fichiers triés par nom :", sorted_files_by_name)
