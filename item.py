from abc import ABC

class Item(ABC):
    def __init__(self, name, id=None):
        self.name = name
        self.id = id