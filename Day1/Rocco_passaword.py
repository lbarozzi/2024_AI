import random
p = str()
def password(): 
    a = ["bernensis", "edwardsi", "majori", "radofilai", "mcgregori"]
    b = random.randint(1,99)
    c = [".", "!", ":", ";", "?"]
    n = random.randint(1,5)
    m = random.randint(1,5)
    x = a[m]
    y = c[n]
    p = x + str(b) + y
    return(p)


    
