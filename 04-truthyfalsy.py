x = 12

print(int(x))
print(str(x))
print(float(x))
print(bool(x))

print(bool(""))

name="asd"
if not name.strip():
  print("Falsy")
else:
  print("Truthy")