import random

number = [random.randint(1, 100) for _ in range(50)]

words = ("Girasole", "Caramella", "Avventura", "Melodia", "Raggio", "Miracolo", "Segreto", "Incanto", "Magia", "Fantasia",
        "Luminescente", "Sirena", "Brezza", "Incantato", "Etereo", "Sogno", "Favola", "Arcano", "Stella", "Splendore",
        "Eclissi", "Crepuscolo", "Alchimia", "Enigma", "Paradiso", "Crepuscolo", "Tramonto", "Fascino", "Aurora", "Riflesso",
        "Miraggio", "Polvere", "Cristallo", "Nuvola", "Rinascita", "Clessidra", "Luce", "Oasi", "Sinfonia", "Sogno",
        "Dolcezza", "Meraviglia", "Risplendente", "Sorriso", "Sospirare", "Incanto", "Profumo", "Selva", "Vortice", "Vento")

names = ("Leone", "Tigre", "Elefante", "Orso", "Rinoceronte", "Ippopotamo", "Giraffa", "Scimmia", "Canguro", "Koala",
    "Panda", "Ghepardo", "Zebra", "Lupo", "Volpe", "Coyote", "Cavallo", "Asino", "Cane", "Gatto",
    "Criceto", "Furetto", "Coniglio", "Scoiattolo", "Tartaruga", "Lucertola", "Serpente", "Pappagallo", "Aquila", "Falco",
    "Pellicano", "Alligatore", "Coccodrillo", "Puma", "Jaguar", "Foca", "Lontre", "Castoro", "Pinguino", "Delfino",
    "Balena", "Squalo", "Tonno", "Anguilla", "Polpo", "Medusa", "Granchio", "Gambero", "Crostaceo", "Ostrica")

car = ("!@#$%^&*()-_+=[]{},.<>?/|")

def password_generator (words, names, number):

    first_word=random.choice(words)
    second_word=random.choice(names)
    rand_number=random.choice(range(1,100))
    rand_car=random.choice(car)

  
    pwd = [first_word,second_word,str(rand_number),str(rand_car)]
    # pass=f"{first_word}{second_word}{str(rand_number)}{str(rand_car)}"
    random.shuffle(pwd)
    password=''.join(pwd)
    
    return password

password = password_generator(words, names, number)
print("Password:", password)


  




