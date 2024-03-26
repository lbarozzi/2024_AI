import random
import string
import os

def uppercase_random_char(word:str)->str:
    idx = random.randint(0, len(word)-1)
    uppercased_word = list(word)
    uppercased_word[idx] = uppercased_word[idx].upper()
    return "".join(uppercased_word)

def sample_of_n_special_char(n:int)->[]:
    return random.sample(string.digits + string.punctuation, n)

def create_password(bag_of_words:list, n_words:int):
    words = random.sample(bag_of_words, n_words)
    words = map(uppercase_random_char, words)
    max_sample_size = 30
    pwd = ''.join(word + random.choice(sample_of_n_special_char(max_sample_size)) for word in words)
    return pwd
    

if __name__ == "__main__":
    with open('bag_of_words.txt') as f:
        bag_of_words = f.read().splitlines()
    pwd = create_password(bag_of_words=bag_of_words, n_words=3)
    print(f'Your password is: {pwd}')
