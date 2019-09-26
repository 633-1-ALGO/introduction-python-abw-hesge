# Problème : Etant donné deux variables c et d, on veut savoir si leur produit est négatif ou positif ou nul.
# Contrainte : Ne pas calculer le produit des deux nombres.
# Résultat attendu : Un message affichant "Produit positif" ou "Produit négatif" ou "Produit nul".
# Indications :  Vous pouvez changer les valeurs des variables pour vos tests.
c = 4444
d = 31

if c < 0 and d < 0:
    print("Produit positif")
elif c < 0 or d < 0:
    print("Produit négatif")
elif c == 0 or d == 0:
    print("Produit nul")
else:
    print("Produit positif")
