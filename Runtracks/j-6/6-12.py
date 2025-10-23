def tri_insertion(tab):
    for i in range(1, len(tab)):
        valeur = tab[i]
        j = i - 1

        while j >= 0 and tab[j] > valeur:
            tab[j + 1] = tab[j]
            j -= 1

        tab[j + 1] = valeur

    return tab

tableau = [8, 3, 5, 1, 9, 2]
print("Avant tri :", tableau)
print("Après tri :", tri_insertion(tableau))
