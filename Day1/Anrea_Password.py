import random

length = 0

words = ["mela",
"banana",
"pollo",
"pasta",
"pizza",
"caffè",
"fiorentina",
"piadina",
"cioccolata"]

punct = [".",
":",
",",
";",
"!",
"?"]

n = 0

p = ""

def password(words, punt):

    p1 = random.choice(punt)
    n1 = random.randint(0,9)
    w1 = random.choice(words)
    n2 = random.randint(0,9)
    w2 = random.choice(words)
    p2 = random.choice(punt)

    pw = p1 + str(n1) + w1 + str(n2) + w2 + p2

    return pw








print(password(words, punct))