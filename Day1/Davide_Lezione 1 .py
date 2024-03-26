import random

from itertools import permutations


#nomi2=()
#piante2=()
#caratteri2=()





nomi = ("Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack",
         "Kate", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rose", "Sam", "Tina",
         "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane", "Sophia", "Ethan", "Ava", "Mason",
         "Isabella", "James", "Emily", "Daniel", "Madison", "Logan", "Abigail", "Benjamin", "Charlotte",
         "Jacob", "Avery", "William", "Ella", "Michael", "Harper", "Alexander", "Amelia", "Elijah")

piante = ("Rosa", "Orchidea", "Girasole", "Tulipano", "Lavanda", "Margherita", "Cactus", "Peperoncino", "Bonsai", "Lillà",
          "Fico", "Olivo", "Bambù", "Sequoia", "Glicine", "Luppolo", "Succulenta", "Rododendro", "Papavero", "Geranio",
          "Aloe", "Camelia", "Dalia", "Felce", "Giaggiolo", "Ibisco", "Kiwi", "Limone", "Mimosa", "Narciso",
          "Ortensia", "Peonia", "Radicchio", "Salice", "Tarassaco", "Uva", "Verbena", "Wisteria", "Yucca",
          "Zafferano", "Zenzero", "Albicocco", "Basilico", "Cedro", "Dente di leone", "Eucalipto", "Fragola",
          "Gelsomino", "Hibiscus")

caratteri= ("#","*","+","&","£","%","§","?","!")

def pssw(lista1,lista2,lista3):
    password = ""
    if len(lista1) and len(lista2) and len(lista3) > 0:
        f = random.randint(0,1000)
        a = lista1[random.randint(0,len(nomi)-1)]
        b = random.randint(0,1000)
        c = lista2[random.randint(0,len(piante)-1)]
        d = random.randint(0,1000)
        e = lista3[random.randint(0,len(caratteri)-1)]
        #a.capitalize
        #c.capitalize
        password =str(f)+ a + str(b) + c + str(d) + e
        #m = list(permutations(password))
        
        return password
    else:
        password = None
        return password

#print(pssw(nomi2,piante2,caratteri2))
print(pssw(nomi,piante,caratteri))
        
    
        