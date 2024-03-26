import random
import string

words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon', 'zucchini']

randomWords = []

def generateRandomPassword():

    for i in range(0, 2):
        randomWord = random.choice(words)

        randindex = random.randint(0, len(randomWord)-1)
        randomWord = randomWord[0:randindex] + randomWord[randindex].upper() + randomWord[randindex+1:]

        randomWords.append(randomWord)
    
    password = randomWords[0] + str(random.randint(0, 9)) + randomWords[1] + str(random.choice(string.ascii_uppercase)) + str(random.choice(string.punctuation))
    print("Random Password is: ", password)
    
    return password

generateRandomPassword()
