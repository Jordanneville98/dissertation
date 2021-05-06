import random

for x in range(10000):
  int1 = str(random.randint(1,220))
  int2 = str(random.randint(1,255))
  int3 = str(random.randint(1,255))
  static = "ip route " + int1+"."+int2+"."+int3+".0" + " 255.255.255.0 null0"
  net_statement = "network " + int1+"."+int2+"."+int3+".0 " + " 0.0.0.255"
  with open("static.txt" , "a") as routes:
    routes.write(static + "\n")
  with open("statements.txt", "a") as statements:
    statements.write(net_statement + "\n")

  print(static)
  print(net_statement)
