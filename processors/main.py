from fuzzify import fuzzifyIPK,fuzzifyPOT,fuzzifyTAN,fuzzifyORG,fuzzifyPRE,viewFuzzified
from rules import rulesMin

ipk = 3.1
tan = 1
pot = 1000000
pre = 1.75
org = 0.55

listIPK,listTAN,listPOT,listORG,listPRE=[],[],[],[],[]

for i in fuzzifyIPK(ipk):
    listIPK.append(i)
for i in fuzzifyTAN(tan):
    listTAN.append(i)
for i in fuzzifyPOT(pot):
    listPOT.append(i)
for i in fuzzifyPRE(pre):
    listPRE.append(i)
for i in fuzzifyORG(org):
    listORG.append(i)

viewFuzzified(listIPK,listTAN,listPOT,listPRE,listORG)


rulesMin(listIPK,listTAN,listPOT,listPRE,listORG)
