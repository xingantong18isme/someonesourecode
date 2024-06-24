t=input("text:")
c=""
while 1:
  if t=="exit":
    break
  for x in t:
    c+=chr(ord(x)^31)
  print(f"Encrypted text is '{c}'")
