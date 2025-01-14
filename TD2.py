import csv
etudiants = [
{"ID": 1, "Nom": "Schmitt", "Prenom": "Albert", "Note": 14},
{"ID": 2, "Nom": "Al-Hakim", "Prenom": "Yasmine", "Note": 17},
{"ID": 3, "Nom": "Tran", "Prenom": "Sebastien", "Note": 12},
{"ID": 4, "Nom": "Meyer", "Prenom": "Claire", "Note": 16},
{"ID": 5, "Nom": "Kobayashi", "Prenom": "Kaito", "Note": 11}
]

with open('donnees.csv', mode='w', encoding='utf-8', newline='') as file:
    champs = ["ID","Nom", "Prenom", "Note"]
    donnees = csv.DictWriter(file, fieldnames=champs)
    donnees.writeheader()
    donnees.writerows(etudiants)