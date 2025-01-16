import json
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

def filtrer_fichiers(infos_triees, TAILLE_MINI_FICHIER_EN_MEGA_OCTET, NB_MAXI_FICHIERS):
    # Convertir la taille minimale en octets
    taille_min_octets = TAILLE_MINI_FICHIER_EN_MEGA_OCTET * 1048576  # 1 Mo = 1048576 octets

    # Filtrer les fichiers dont la taille est supérieure à la taille minimale spécifiée
    fichiers_filtres = [fichier for fichier in infos_triees if fichier[2] >= taille_min_octets]

    # Limiter le nombre de fichiers à NB_MAXI_FICHIERS
    fichiers_filtres = fichiers_filtres[:NB_MAXI_FICHIERS]

    return fichiers_filtres

def creer_fichier_json(liste_fichiers, nom_fichier_json):
    # Remplacer les antislashs par des doubles antislashs dans le chemin
    for liste_fichier in liste_fichiers:
        liste_fichier[0] = liste_fichier[0].replace('\\', '\\\\')

    # Ouvrir le fichier en mode écriture et y enregistrer la liste au format JSON
    with open(nom_fichier_json, 'w', encoding='utf-8') as f:
        json.dump(liste_fichiers, f, indent=4)


# Récupérer les info des fichiers
infos = liste_fichier()

# Trier les informations par taille
infos_triees = trier_par_taille(infos)

#Filtré les infos
infos_filtees = filtrer_fichiers(infos_triees, 0, 100) #A COMPLETER !!!

# Afficher les résultats triés
for info in infos_filtees:
    print(f"Chemin : {info[0]}, Nom : {info[1]}, Taille : {info[2]} octets")

creer_fichier_json(infos_filtees, "fichiers.json")