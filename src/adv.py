from room import Room
from item import Items
from player import Player
import textwrap
# Declare all the rooms

item = {
    'sword': Items("Sword of Destiny", "fight your way through any challenge"),
    'scroll': Items("Ancient Scroll", "This ancient scroll might come in handy"),
    'key': Items("Skeleton Key", "Unlock any room"),
    'coin': Items("Golden Coin", "A Taste of the treasure that awaits you"),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#append items to rooms
room['overlook'].add_items(item['sword'])
# room['overlook'].add_items(item['key'])
# room['foyer'].add_items(item['coin'])
room['foyer'].add_items(item['scroll'])
print(room['overlook'].items)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

p1 = None
r  = None

def print_start(p1):
    print(f'Hello {p1.name}, welcome to your new adventure. You are currently {p1.rName}, {p1.information} ') 

def print_room(p1):
    wrapper = textwrap.TextWrapper(width=40)
    info = wrapper.wrap(text=p1.information) 
    print(f'{p1.name}, you are now in the {p1.rName}')
    for element in info: 
        print(f'\033 {element} \033') 

def item_loop(item, p1, room):
    print(f"There are {len(item)} item(s) in this room:")
    for l in item:
        if(bool(l)):
            command = input(f"{l} type 'get item' to add to inventory or 'drop item' to leave in room:")
            result = command.split(" ")
            for i, j in enumerate(result):
                if j == "get":
                    p1.add_items(item[i])
                    room.drop_items(item[i])
                    print(f"you now have {p1.inventory[i].name} in your inventory")
                    print(f"There are now {len(item)} items in this room:")
                # if j == "drop":
                #     p1.remove("item")
                #     print("you dropped an item")
            
def room_input():
    global r
    r = input("Choose your destination [n] North [e] East [s] South [w] West [q] quit: ")

def player_story(item, p1, room, d):
    p1.rName = d.rName
    p1.information = d.information
    print_room(p1)
    item_loop(item, p1, room)
    room_input()


def get_name():
    name = input("Please enter your name: ")
    p1 = Player(name, room['outside'].rName, room["outside"].information)
    print_start(p1)
    global r
    def move():
        foyer = room['foyer']
        narrow = room['narrow']
        outside = room['outside']
        overlook = room['overlook']
        treasure = room['treasure']
        nonlocal p1
        room_input()
        global r
        while not r == "q":
            # User chooses North to Foyer
            if r == "n":
                player_story(foyer.items, p1, foyer, outside.n_to)
                if r == "s":
                    player_story(outside.items, p1, outside, foyer.s_to)
                elif r == "n":
                     # User Chooses North goes from Foyer to Overlook
                    player_story(overlook.items, p1, overlook, foyer.n_to)
                    if r == "s":
                         # User Chooses South goes from Overlook to Foyer
                        player_story(foyer.items, p1, foyer, overlook.s_to)
                    else:
                        print('You cannot go in that direction!')
                elif r == "e":
                    # User Chooses East goes from Foyer to Narrow
                    player_story(narrow.items, p1, narrow, foyer.e_to)
                    if r == "w":
                        # User Chooses West goes from Narrow to Foyer
                        player_story(foyer.items, p1, foyer, narrow.w_to)
                    elif r == "n":
                        # User Chooses North goes from Narrow to Treasure
                        player_story(treasure.items, p1, treasure, narrow.n_to)
                        if r == "s":
                            # User Chooses South goes from Treasure to Narrow
                            player_story(narrow.items, p1, narrow, treasure.s_to)
                else:
                    print('You cannot go in that direction!')
                    room_input()
            else:
                print("You cannot go in that direction!")
                r = input("Choose your destination [n] North [e] East [s] South [w] West [q] quit: ")
    move()
get_name()


