class Shark: #Shark is the defined class
    def __init__(self, name): 
        self.name = name

    def swim(self):
        print(self.name + " is swimming.")#Mehthod be awsome is created, concatenation allows the text "swim" and the name of the shark "stevie" object to be printed.

    def be_awesome(self):
        print(self.name + " is being awesome.")#Mehthod be awsome is created, concatenation allows the text "be awesome" and the name of the shark "sammy" object to be printed.
    
    def is_eating(self):
        print(self.name + " is eating.")#Mehthod be awsome is created, concatenation allows the text "eating" and the name of the shark "cameron" object to be printed.

def main():
    sammy = Shark("Sammy")#Named the shark object as Sammy
    sammy.be_awesome()
    stevie = Shark("Stevie")#Named the shark object as Stevie
    stevie.swim()
    cameron = Shark("Cameron")#Named the shark object as Cameron
    cameron.is_eating()
    
if __name__ == "__main__":#
  main()
