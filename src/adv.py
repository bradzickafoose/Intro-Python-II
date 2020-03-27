from room import Room
from player import Player
from item import Item

# Declare all the rooms

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


def moves(self, move):
    if move == 'n':
        return self.current_room.n_to
    elif move == 's':
        return self.current_room.s_to
    elif move == 'e':
        return self.current_room.e_to
    else:
        return self.current_room.w_to


def main():
    player = Player(input("\nEnter your adventurer name: "), room['outside'])
    print('\n**************************************\n')
    print(f"** Welcome to Adventure Land, {player.name}! **")
    print('\n**************************************')
    while True:
        print(f"\nYou are currently in the {player.current_room.name}.")
        print(f'{player.current_room.description}')
        print(
            '\nWhere would you like to go? [n] North [s] South [e] East [w] West or [q] Quit')
        cmd = input('-> ')
        if cmd == 'q':
            print('\nThank you for visiting Adventure Land\n')
            break
        elif cmd == 'n' or cmd == 's' or cmd == 'e' or cmd == 'w':
            if moves(player, cmd) is None:
                print('\n*************************************************')
                print(f'\nYou can\'t go that way, {player.name}!')
                print('Try a different direction.')
                print('\n*************************************************')
                continue
            else:
                player.current_room = moves(player, cmd)
        else:
            print(
                'Please enter a valid direction: [n] North [s] South [e] East [w] West or [q] Quit')
            continue


if __name__ == '__main__':
    main()
