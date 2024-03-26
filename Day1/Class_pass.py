import random
import json
from json import JSONEncoder

class PasswordGenerator():
    generated = 0

    def __init__(self, tupA=tuple(), tupB=tuple(),special='.,:,-_@#§&/%$£!'):
        print("Init Passwd Generator")
        self.wordA= tupA
        self.wordB = tupB 
        self.special = special
        self.maxNum=9
        self.shuffle=True
   
    def choice(self, lista):
        return  self.RandCase(str(random.choice(lista) )
                         .replace(" ","")
                         )

    def RandCase(self,testo):
        idx = random.randint(0, len(testo) - 1)
        return testo[:idx] + testo[idx].upper() + testo[idx + 1:]

    def makePasswd(self):
        PasswordGenerator.generated+=1
        lst= [
            self.choice(self.wordA),
            self.choice(range(0,self.maxNum)),
            self.choice(self.wordB),
            self.choice(self.special)
        ]
        
        
        if self.shuffle:
            random.shuffle(lst)

        return "".join(lst)
    
    def __str__(self):
        return f"A= {len(self.wordA)} B: {len(self.wordA)} generated = {PasswordGenerator.generated}"
    

def main():
    GenA=  PasswordGenerator()
    GenA.wordA = ("apple", "banana", "orange", "mango", "grapefruit", "kiwi", "watermelon", 
         "strawberry", "blueberry", "pineapple", "honeydew", "coconut", 
         "papaya", "guava", "nectarine", "plum", "apricot", "cherry", "peach", "fig", 
         "date", "pomegranate", "lychee", "longan", "rambutan", "dragonfruit", "starfruit", 
         "persimmon")

    GenA.wordB  = (
       "phone", "laptop", "chair", "desk", "lamp", "pen", "pencil", "paper", "book", "cup",
        "plate", "fork", "knife", "spoon", "wallet", "keys", "watch", "glasses", "shirt",
        "pants", "shoes", "bag", "bed", "pillow", "blanket", "sofa", "table", "television",
        "computer", "printer", "fridge", "stove", "microwave", "coffee maker",
        "toaster", "blender", "toothbrush", "shampoo", "soap", "towel", "mirror",
        "car", "bike", "bus", "train", "money"
    )
    GenB=  PasswordGenerator()
    GenB.wordA = ("mela", "banana", "arancia", "mango", "pompelmo", "kiwi", "anguria", 
            "fragola", "mirtillo", "ananas", "melone cantalupo", "melone honeydew", "cocco", 
            "papaia", "guava", "nettarina", "prugna", "albicocca", "ciliegia", "pesca", "fico", 
            "dattero", "melagrana", "lychee", "longan", "rambutan", "frutto del drago", "carambola", 
            "cachi")

    GenB.wordB  = (
        "telefono", "computer portatile", "sedia", "scrivania", "lampada", "penna", "matita", "carta", "libro", "tazza",
        "piatto", "forchetta", "coltello", "cucchiaio", "portafoglio", "chiavi", "orologio", "occhiali", "camicia",
        "pantaloni", "scarpe", "borsa", "letto", "cuscino", "coperta", "divano", "tavolo", "televisione",
        "computer", "stampante", "frigorifero", "stufa", "forno a microonde", "aspirapolvere", "macchina del caffè",
        "tostapane", "frullatore", "asciugacapelli", "spazzolino da denti", "shampoo", "sapone", "asciugamano", "specchio",
        "macchina", "bicicletta", "autobus", "treno", "soldi"
    )

    print(GenA.makePasswd() );
    print(GenA)

    print(json.dumps(GenA.__dict__))
    
    print(GenB.makePasswd() );
    print(GenA)
    print(GenB)
    # pass

if __name__=="__main__":
    main()