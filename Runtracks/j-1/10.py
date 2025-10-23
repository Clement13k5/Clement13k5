montant_initial=5000
taux_annuel=0.05

m1=montant_initial*taux_annuel
montant_initial+=m1
print(montant_initial)

montant_initial+=5000
taux_annuel+=0.02
m2=montant_initial*taux_annuel
montant_initial+=m2
print(montant_initial)

m3=montant_initial*0.9
taux_annuel-=0.01
m3=montant_initial*taux_annuel
montant_initial+=m3
print(montant_initial)
