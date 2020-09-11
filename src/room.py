# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, rName, information):
        self.rName = rName
        self.information = information
        self.items = []
    def add_items(self, item):
        self.items.append(item)
    def drop_items(self, item):
        self.items.remove(item)
    def __str__(self): 
        return self
