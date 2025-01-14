import csv
etudiants = [
{"ID": 1, "Nom": "Schmitt", "Prénom": "Albert", "Note": 14},
{"ID": 2, "Nom": "Al-Hakim", "Prénom": "Yasmine", "Note": 17},
{"ID": 3, "Nom": "Tran", "Prénom": "Sebastien", "Note": 12},
{"ID": 4, "Nom": "Meyer", "Prénom": "Claire", "Note": 16},
{"ID": 5, "Nom": "Kobayashi", "Prénom": "Kaito", "Note": 11}
]

with open('donnees.csv', mode='w', encoding='utf-8', newline='') as file:
    donnees = csv.writer(file)
    donnees.writerows(etudiants)