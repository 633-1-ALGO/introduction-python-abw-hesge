# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 444, 5, 777, 2], [23, 24, 15, 75, 23]]
val = 0
ii = 0
jj = 0
for i in range(0, len(tab)):
    for j in range(0, len(tab[i])):
        if val < tab[i][j]:
            val = tab[i][j]
            ii = i
            jj = j
print ("La valeur maximum est", val, "et elle se trouve à l'indice [", ii, "][", jj, "]")
