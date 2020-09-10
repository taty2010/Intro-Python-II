# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, rName, information):
        self.rName = rName
        self.information = information
        def __str__(self): 
            return self