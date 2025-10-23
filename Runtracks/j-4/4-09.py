
def moyenne (note1,note2,note3):
  moyenne_etudiants= (note1+note2+note3)/3
  if moyenne_etudiants>=15:    
    return "TB"
  elif 11<=moyenne_etudiants<=14:
    return "B"
  elif 8<=moyenne_etudiants<=10:
    return "Mid"
  else:
    return "fais des efforts"
  
print(moyenne(12,15,14))#B
print(moyenne(1,5,4))#effort
print(moyenne(17,15,19))#TB
print(moyenne(9,8,10))#mid