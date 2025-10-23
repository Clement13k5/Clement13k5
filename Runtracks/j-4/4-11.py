def time_to_text (min):
  heure=min//60
  minutes=min%60
  return heure,"h",minutes, "min"

print(time_to_text(124))