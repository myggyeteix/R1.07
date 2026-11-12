x = float(input("Entrer un multiplicateur : "))
l_rslt = []
for i in range(10):
    l_rslt.append(round((x * i),1))
    print(x,"*",i,"=",l_rslt[i])
