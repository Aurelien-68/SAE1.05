from pathlib import Path
def liste_fichier():
    # Crée un objet Path pour le répertoire de base
    repertoire_de_base = Path.cwd()

    # Liste pour stocker les informations sur les fichiers
    infos_fichiers=[]


    # Liste les fichiers et sous-répertoires du répertoire
    for fichier in repertoire_de_base.iterdir():
        chemin_fichier = Path(fichier)
        nom_fichier = fichier
        taille_fichier = chemin_fichier.stat().st_size  # Taille en octets
        infos_fichiers.append([chemin_fichier, nom_fichier, taille_fichier])
    return infos_fichiers


infos = liste_fichier()
print(infos)