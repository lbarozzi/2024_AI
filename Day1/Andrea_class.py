import random


class GenPassword():
    def __init__(self):
        self.words = tuple()
        self.punct = tuple()

    def password(self):
        p1 = random.choice(self.punct)
        n1 = random.randint(0,9)
        w1 = random.choice(self.words)
        n2 = random.randint(0,9)
        w2 = random.choice(self.words)
        p2 = random.choice(self.punct)
        pw = p1 + str(n1) + w1 + str(n2) + w2 + p2
        return pw

    


def main():
    Password1 = GenPassword()
    Password1.words = ("mela", "banana", "pollo", "pasta", "pizza", "caffè", "fiorentina", "piadina", "cioccolata")
    Password1.punct = (".", ":", ",", ";", "!", "?")
    print(Password1.password())
    
    # pass


main()