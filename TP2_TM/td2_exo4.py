base = 4
nbConvives = int(input("Nombres de convives : "))

fromage = 800.0
nv_fromage = fromage * nbConvives / base

eau = 2
nv_eau = eau * nbConvives / base

ail = 2
nv_ail = ail * nbConvives / base

pain = 400
nv_pain = pain * nbConvives / base

print(f"Pour {nbConvives} convives, il faut : fromage --> {nv_fromage} gr, eau --> {nv_eau} dl, ail --> {nv_ail} gousse(s), "
      f"pain --> {nv_pain} gr")
