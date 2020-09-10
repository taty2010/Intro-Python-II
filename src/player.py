# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player(Room):
    def __init__(self, name, rName, information):
        super().__init__(rName, information)
        self.name = name
        self.prevRoom = []
        def previous_rooms(self, room):
            history = Room(room, self)
            self.prevRoom.append(history)