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
    print(f"There are {len(item)} items in this room:")
    print(item)
    for l in item:
        if(bool(l)):
            command = input(f"{l} type 'get item' to add to inventory or 'drop item' to leave in room:")
            result = command.split(" ")
            for i, j in enumerate(result):
                if j == "get":
                    p1.add_items(item[i])
                    room.drop_items(item[0])
                    print(f"you now have {p1.inventory[i].name} in your inventory")
                    print(f"There are now {len(item)} items in this room:")
                # if j == "drop":
                #     p1.remove("item")
                #     print("you dropped an item")
            

def room_input():
    global r
    r = input("Choose your destination [n] North [e] East [s] South [w] West [q] quit: ")

def pickup_items(p1, item):
    print(f'{p1.name}, you added {item} to your inventory')

def get_name():
    name = input("Please enter your name: ")
    p1 = Player(name, room['outside'].rName, room["outside"].information)
    print_start(p1)
    global r
    def move():
        nonlocal p1
        room_input()
        global r
        while not r == "q":
            # User chooses North to Foyer
            if r == "n":
                foyer = room['foyer']
                narrow = room['narrow']
                p1.rName = room['outside'].n_to.rName
                p1.information = room['outside'].n_to.information
                print_room(p1)
                item_loop(foyer.items, p1, room['outside'])
                room_input()
                # User Chooses South goes from Foyer to Outside
                if r == "s":
                    p1.rName = foyer.s_to.rName
                    p1.information = foyer.s_to.information
                    print_room(p1)
                    item_loop(foyer.s_to.items)
                    room_input()
                elif r == "n":
                     # User Chooses North goes from Foyer to Overlook
                    p1.rName = foyer.n_to.rName
                    p1.information = foyer.n_to.information
                    print_room(p1)
                    item_loop(foyer.n_to.items)
                    room_input()
                    if r == "s":
                         # User Chooses South goes from Overlook to Foyer
                        p1.rName = room['overlook'].s_to.rName
                        p1.information = room['overlook'].s_to.information
                        print_room(p1)
                        item_loop(room['overlook'].s_to.items)
                        room_input()
                    else:
                        print('You cannot go in that direction!')
                elif r == "e":
                    # User Chooses East goes from Foyer to Narrow
                    p1.rName = foyer.e_to.rName
                    p1.information = foyer.e_to.information
                    print_room(p1)
                    item_loop(foyer.e_to.items)
                    room_input()
                    if r == "w":
                        p1.rName = narrow.w_to.rName
                        p1.information = narrow.w_to.information
                        print_room(p1)
                        item_loop(narrow.w_to.items)
                        room_input()
                    elif r == "n":
                        p1.rName = narrow.n_to.rName
                        p1.information = narrow.n_to.information
                        print_room(p1)
                        item_loop(narrow.n_to.items)
                        room_input()
                        if r == "s":
                            p1.rName = room['treasure'].s_to.rName
                            p1.information = room['treasure'].s_to.information
                            print_room(p1)
                            item_loop(room['treasure'].s_to.items)
                            room_input()
                else:
                    print('You cannot go in that direction!')
                    room_input()
            else:
                # print("You cannot go in that direction!")
                r = input("Choose your destination [n] North [e] East [s] South [w] West [q] quit: ")
    move()
get_name()


