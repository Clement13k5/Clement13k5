def dev (languages):
  if languages=="java":
    return "t'es developer logiciel"
  elif languages=="python":
    return "t'es developper IA"
  elif languages=="javascript":
    return "t'es developper web"
  elif languages=="reactjs":
    return "t'es developper mobile"
  else:
    return "un jour je serais le mailleur developper"
  

print(dev("python"))
