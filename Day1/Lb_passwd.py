import random

frutta = ("mela", "banana", "arancia", "mango", "pompelmo", "kiwi", "anguria", 
         "fragola", "mirtillo", "ananas", "melone cantalupo", "melone honeydew", "cocco", 
         "papaia", "guava", "nettarina", "prugna", "albicocca", "ciliegia", "pesca", "fico", 
         "dattero", "melagrana", "lychee", "longan", "rambutan", "frutto del drago", "carambola", 
         "cachi")

cose  = (
    "telefono", "computer portatile", "sedia", "scrivania", "lampada", "penna", "matita", "carta", "libro", "tazza",
    "piatto", "forchetta", "coltello", "cucchiaio", "portafoglio", "chiavi", "orologio", "occhiali", "camicia",
    "pantaloni", "scarpe", "borsa", "letto", "cuscino", "coperta", "divano", "tavolo", "televisione",
    "computer", "stampante", "frigorifero", "stufa", "forno a microonde", "aspirapolvere", "macchina del caffè",
    "tostapane", "frullatore", "asciugacapelli", "spazzolino da denti", "shampoo", "sapone", "asciugamano", "specchio",
    "macchina", "bicicletta", "autobus", "treno", "soldi"
)

def choice(lista):
    return  RandCase(str(random.choice(lista) )
                         .replace(" ","")
                         )

def RandCase(testo):
    idx = random.randint(0, len(testo) - 1)
    return testo[:idx] + testo[idx].upper() + testo[idx + 1:]

def makePasswd(shuffle=True):
    lst= [
        choice(frutta),
        choice(range(0,9)),
        choice(cose),
        choice('.,:,-_@#§&/%$£!')
    ]
    
    
    if shuffle:
        random.shuffle(lst)

    return "".join(lst)
    

def main():
    print("Ciao Mamma")
    print(makePasswd())

if __name__=="__main__":
    main()