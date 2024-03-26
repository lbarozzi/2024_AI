from random import randint
import random
import time

random.seed(time.time())

class Pwd_generator:

    def __init__(self, List1, List2):
        self.Format = {"List1" : 1, "List2" : 1, "Numbers" : 3, "Special chr" : 3}
        self.List1 = List1
        self.List2 = List2
        
    '''
    genera una password con le liste fornite durante l'inizializzazione
    upper -> se True(default) capitalizza alcune lettere in maniera casuale 
    '''
    def get_pwd(self, upper = True):
        # Creo una copia dei dati per non modificare quelli della classe
        Format = self.Format
        List1 = self.List1
        List2 = self.List2
        ret = ''
        
        # Genero i token del formato richiesto in ordine sparso, finchè il dizionario non è "vuoto"
        while(not all(x==0 for x in Format.values())):

            #estraggo il tipo di token
            t = randint(0, 4)

            # Genero il token del tipo scelto, ed aggiorno il dizionario
            if(t == 0 and Format["List1"] > 0):
                y = randint(1, len(List1)-1)
                ret += List1.pop(y)    
                Format["List1"] -=1   

            if(t == 1 and Format["List2"] > 0):
                y = randint(1, len(List2)-1)
                ret += List2.pop(y)
                Format["List2"] -=1    

            if(t == 2 and Format["Numbers"] > 0):
                ret += str(randint(1, 9))
                Format["Numbers"] -=1    

            if(t == 3 and Format["Special chr"] > 0):
                ret += chr(randint(33, 47))
                Format["Special chr"] -=1

        if(upper):
            # Cambia lettere a caso in maiuscolo
            for i in range(len(ret)):
                if(randint(0,1) == 0):
                    ret = ret[:i] + ret[i].upper() + ret[i+1:]

        return ret
    
    '''
    ritorna una stringa esplicativa del formato
    '''
    def __str__(self):
        return "hello world"

if __name__ == "__main__":

    first = Pwd_generator(["carbonara", "pecorino", "uova", "patate", "zucchina", "cipolla"], 
                          ["jackson", "mercury", "lamar", "swift", "joseph", "harrison", "rodrigo"])

    second = Pwd_generator(["arancio", "blu", "viola", "giallo", "nero", "marrone"], 
                           ["jhon", "ted", "nick", "schmidt", "frodo", "obi", "peter"])

    # Generazione password
    print("primo  : ", first.get_pwd())
    print("secondo: ", second.get_pwd())
    


