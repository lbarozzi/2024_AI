animali_rari_1 = (
    "quokka", "axolotl", "okapi", "narvalo", "cassowary", "tarsio", "coati", "vaquita", "pangolino", "fennec",
    "jerboa", "binturong", "oryx", "manul", "dugongo", "cuscus", "saola", "solenodonte", "takin", "galago",
    "numbat", "tapir", "bongo", "quoll", "cacomistle", "aye-aye", "ibex", "tayra", "dhole", "fossa", "sifaka",
    "kiwi", "shoebill", "tamaraw", "markhor", "serval", "capybara", "muntjac", "mara", "pika",
    "baiji", "gharial", "gerenuk", "whitefish", "squid", "coelacanth", "crab", "squid",
    "tardigrade"
)

animali_rari_2 = (
    "curioso", "unicorno", "misterioso", "veloce", "agile", "colorato", "vivace", "tranquillo", "adorabile", "saltellante",
    "gracile", "elegante", "selvatico", "gigante", "soffice", "imponente", "magico", "strano", "scaltro", "intrepido",
    "robusto", "saggio", "affascinante", "fascinoso", "inquietante", "eccentrico", "audace", "furbo", "flessibile", "intelligente",
    "meraviglioso", "adorabile", "maestoso", "fiero", "aggraziato", "giovane", "piccolo", "velenoso", "carino", "indomabile", 
    "bizzarro", "allegro", "forte", "nobile", "feroce", "leggendario", "resistente", "misterioso", "simpatico"
)

simboli = ("+", "-", "*", "/", "=", "<", ">", "&", "|", "%", "^")
numeri = tuple(range(1, 21))


import random 
animali_1 = random.choice(animali_rari_1)
indice_lettera = random.randint(0, len(animali_1)-1)
animali_1_nuovo = animali_1[:indice_lettera] + animali_1[indice_lettera].upper() + animali_1[indice_lettera+1:]

animali_2 = random.choice(animali_rari_2)
indice_lettera_2 = random.randint(0, len(animali_2)-1)
animali_2_nuovo = animali_2[:indice_lettera_2] + animali_2[indice_lettera_2].upper() + animali_2[indice_lettera+1:]

crea_password = [animali_1_nuovo, random.choice(simboli), animali_2_nuovo, str(random.choice(numeri))]
random.shuffle(crea_password)
password = ''.join(crea_password)
print("la password è :",password)



  

