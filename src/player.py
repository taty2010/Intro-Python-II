# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.prevRoom = []
        def previous_rooms(self, room):
            history = Room(room, self)
            self.prevRoom.append(history)