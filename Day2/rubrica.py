from class_rubrica import Item,Rub

def GetItem():
    f=input("Firstname:")
    l=input("LastName:")
    p=input("Phone:")
    d=input("DOB:")
    a=input("Address:")
    c=input("City:")
    return Item(f,l,p,d,a,c)

def Menu():
    print("1: List")
    print("2: Add")
    print("3: Delete")
    print("")
    print("")
    print("0: Exit")
    return input("Choice:")

def ShowList(rub):
    # for a,k in rub.items():
    for k in rub.values(): 
        print(f'{k}')

def delete(rub):
    ShowList(rub)
    key=input("Wich key?: ")
    if(key in rub):
        del rub[key]


def main():
    Rubrica= Rub()
    m=Item("Leonardo","Barozzi","555-55555","23/03/1972","via da qui","Milano")
    Rubrica[m.key()]=m

    res=Menu()
    while res!='0':
        if(res=='1'):
            ShowList(Rubrica)
        elif res=='2':
            i= GetItem()
            Rubrica[i.key()]=i
        elif res=='3':
            delete(Rubrica)
        res=Menu()


    

    ShowList(Rubrica)

    # tmp = Rubrica.piklout()
    tmp =Rubrica.dump_json()
    print(tmp)

    #v=Rub.unpikle(tmp)
    v= Rubrica.from_json(tmp)

    ShowList(v)
    pass

if __name__=="__main__":
    main()