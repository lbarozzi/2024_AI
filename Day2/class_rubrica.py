import csv
import json
import pickle

class Item:
    def __init__(self,First="",Last="",Phone="",DOB=None,Address="",City=""):
        # super.__init__()
        self.FirstName=First
        self.LastName=Last
        self.Phone=Phone
        self.DOB=DOB
        self.Address=Address
        self.City=City
    
    def key(self):
        return f"{self.LastName[:2]}{self.FirstName[:2]}" #-{self.LastName}{self.FirstName}"
    
    def __str__(self):
        return f"{self.key()}: {self.FirstName} {self.LastName} @ {self.City}"

class ItemEncoder(json.JSONEncoder):
    def default(self, obj):
        print(type(obj).__name__)
        if isinstance(obj, Item):
            return obj.__dict__
        
        return json.JSONEncoder.default(self, obj)

class Rub(dict):
    '''
    def __init__(self):
        dict.__init__(self)
        super(dict).__init__()
    #'''

    def dump_json(self):
        lst=tuple(self.values())
        '''
        for k,v in self.items():
            lst.append( json.dumps(v,cls=ItemEncoder))
        # '''

        '''
        for a in self:
            lst.append( json.dumps(self[a],cls=ItemEncoder)) 
        # '''
        return json.dumps(lst,cls=ItemEncoder) 

    @classmethod
    def from_json(cls,data):
        s=Rub()
        lst = json.loads(data)
        for d in lst:
            v=Item(d["FirstName"],d["LastName"],d["Phone"],d["DOB"],d["Address"],d["City"])
            s[v.key()]=v
        return s

    def piklout(self):
        return pickle.dumps(self)
    
    @classmethod
    def unpikle(cls,Data):
        return pickle.loads(Data)
