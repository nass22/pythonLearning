# SECTION  - Exercice 105

nom_chauffeur = ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
distance_chauffeur_km = [1.5, 2.2, 0.9, 0.4, 7.1, 1.1, 0.6]

distance_min = distance_chauffeur_km[0]

for distance in distance_chauffeur_km:
    if distance < distance_min:
        distance_min = distance

index_min = distance_chauffeur_km.index(distance_min)

print("Distance minimale:", distance_min, "km")
print("Index de la distance minimal:", index_min)
print("Nom du chauffeur le plus proche:", nom_chauffeur[index_min])