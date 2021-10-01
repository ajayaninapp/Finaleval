class Pet:

    def __init__(self,name="",species=""):

        self.name=name
        try:
            self.species=species
            if species not in [ 'dog', 'cat', 'horse', 'hamster']:
                raise ValueError('Not in List of species')
        except (ValueError, IndexError):
            exit('Non valid species')

    def __str__(self) :
        if self.name!="":
            return f'Species of {self.species},named{self.name}'
        else:
             return f'Species of {self.species}Unnamed\n'



class Dog(Pet):
    def __init__(self, name="",chases="cat"):
        super().__init__(name=name, species="dog")
        self.chases=chases
    def __str__(self) :
        if self.name!="":
            return f'Dog named named\t{self.name},\t chases\t{self.chases}'
        else:
             return f'Unnamed dog chases\t{self.chases}\n'

class Cat(Pet):
    def __init__(self, name="",hates="dogs"):
        super().__init__(name=name, species="cat")
        self.hates=hates
    def __str__(self) :
        if self.name!="":
            return f'Cat named\t{self.name},\t Hates{self.hates}'
        else:
             return f'Unnamed Cat hates\t{self.hates}\n'
dict={"dog":[],"cat":[]}
dogs=[]
cats=[]
for i in range (0,4):
    name=input("enter dog name")
    newDog=Dog(name)
    dogs.append(newDog)
    dict["dog"].append(dogs[i])
for i in range (0,3):
    name=input("enter cat name")
    newCat=Cat(name)
    cats.append(newCat)
    dict["cat"].append(cats[i])


print(dict["dog"])
print(dict["cat"])







        