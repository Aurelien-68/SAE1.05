from pathlib import Path
def liste_fichier():
    # Crée un objet Path pour le répertoire de base
    repertoire_de_base = Path.cwd()

    # Liste pour stocker les informations sur les fichiers
    infos_fichiers=[]


    # Liste les fichiers et sous-répertoires du répertoire et leurs taille en octets
    for fichier in repertoire_de_base.iterdir():
        if fichier.is_file():  # pour s'assurer que c'est bien un fichier et pas un repertoire
            chemin_fichier = str(fichier)  # Convertir le chemin en chaîne de caractères
            nom_fichier = fichier.name  # Extraire le nom du fichier sans son chemin
            taille_fichier = fichier.stat().st_size  # Taille en octets
            infos_fichiers.append([chemin_fichier, nom_fichier, taille_fichier])
            return infos_fichiers

# Trie la liste en fonction de la taille (le troisième élément), de manière décroissante
def trier_par_taille(infos_fichiers):
    # Trier la liste par la taille
    return sorted(infos_fichiers, key=lambda x: x[2], reverse=True)

# Récupérer les info des fichiers
infos = liste_fichier()

# Trier les informations par taille
infos_triees = trier_par_taille(infos)

# Afficher les résultats triés
for info in infos_triees:
    print(f"Chemin : {info[0]}, Nom : {info[1]}, Taille : {info[2]} octets")