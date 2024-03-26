import random
import time

random.seed(time.time())
ret = ''

#liste di parole che si intendono usare, potrebbero riguardare il campo in cui vengono usate per semplificarne la memorizzazione
#una lista potrebbe essere composta solo di aggettivi, mentre l'altra solo di sostantivi, o altre combinazioni simili
list1 = ["carbonara", "pecorino", "uova", "patate", "zucchina", "cipolla"]
list2 = ["jackson", "mercury", "lamar", "swift", "joseph", "harrison", "rodrigo"]

#lista per decidere quanti elementi di ciascun tipo si vogliono
#0->list1
#1->list2
#2->numeri
#3->caratteri
types = [0, 1, 2, 2, 2, 3, 3, 3]

while(len(types) > 0):
    #sceglie che tipo di chiave inserire
    Rand = random.randint(0, len(types)-1)
    t = types.pop(Rand)

    #inserisce la chiave scelta
    if(t == 0):
        x = random.randint(1, len(list1)-1)
        ret += list1.pop(x)        
    if(t == 1):
        x = random.randint(1, len(list2)-1)
        ret += list2.pop(x)
    if(t == 2):
        ret += str(random.randint(1, 9))
    if(t == 3):
        ret += chr(random.randint(33, 47))

#cambia lettere a caso in maiuscolo
for i in range(len(ret)):
    if(random.randint(0,1) == 0):
        ret = ret[:i] + ret[i].upper() + ret[i+1:]

print(ret)
