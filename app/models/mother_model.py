from abc import ABC, abstractmethod

class AbstractParent(ABC):
    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError

    def greet(self):
        raise NotImplementedError

class Mother(AbstractParent):
    def __init__(self, age):
        self.age = age
        print("mother constructor")

    def do_work(self):
        print("I'm working")

    def greet(self):
        print("Hello daughter")

    def do_house_work(self):
        print("Listening music")


class Father(AbstractParent):

    def __init__(self):
        print("father constructor")

    def play_guitar(self):
        print("play guitar")

    def do_house_work(self):
        print("sitting ont he sofa and drink beer")

class Friend:
    pass

class Daughter(Mother, Father):

    def __init__(self, age = 0):
        Father.__init__(self)
        Mother.__init__(self, age=age)

    def do_work(self):
        print("I'm working like a horse")

    def hello_friend(self):
        pass

def greet_mother(mother : Mother):
    print("Hello mother!")
    mother.do_work()

def greet_father(father : Father):
    print("Hello father!")
    father.play_guitar()

if __name__ == "__main__":
    daughter = Daughter()

    #change object class
    #daughter.__class__ = Friend

    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_house_work()

    for x in [daughter]:
        x.do_house_work()

    #list
    povtorka_list = ["mathan_2", "programming_2", "superprise"]

    #taple
    vasian = ("11 years", 12, 3.14, daughter)

    #set
    my_set = {23, 11, 10, 10, "call"}
    print(my_set)

    #frozen set
    another_set = frozenset(["di_", "mi", "do"])

    #dictionary
    my_dict = {1: "first", "2": 123, (1, 2, 3): "tuple_as_a_key"}