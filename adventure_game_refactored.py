import time
import random

TIME_SPEED = .2

NORTH = "n"
SOUTH = "s"
EAST = "e"
WEST = "w"

list_of_valid_cardinal_directions = [NORTH, SOUTH, EAST, WEST]

YES_RESPONSE = ["yes", "y", "yep"]
NO_RESPONSE = ["no", "n", "nope"]

KITCHEN = ["the kitchen", "It smells like something's burning..."]
CORRIDOR = ["a corridor", ("A light at the end of the hallway "
                           "piques your curiosity")]
GALLERY = ["the gallery of secrets", ("The room is full of mysterious "
                                      "cabinets, secured with an array of "
                                      "fancy padlocks.")]
ARBORETUM = ["the arboretum", ("The sumptuous fruit trees are tempting..."
                               "until you notice the feasting worms.")]
FREEZER = ["the walk-in freezer", ("The freezer has a detrimental effect on "
                                   "your proton pack's battery life.")]
ROTUNDA = ["the rotunda", ("You are surrounded by statues and "
                           "suits of armor.\n"
                           "You clap to test the room echo, and "
                           "are taken aback as one of the heads "
                           "swivels to investigate.")]
LIBRARY = ["the library", ("Bookshelves line every wall from "
                           "floor to ceiling\n"
                           "Surely there's a secret passageway "
                           "in here somewhere...")]
BROOM_CLOSET = ["the broom closet", ("You never knew one person "
                                     "could own so many brooms.")]
DISCO = ["the discotheque", ("The floor is littered with glitter and "
                             "forgotten shoes from the previous night.\n"
                             "Strangely no one seems to "
                             "remember what happened...")]
BATHROOM = ["a particularly lavish bathroom", ("The golden fixtures and "
                                               "marble toilet dazzle you..."
                                               "and then you notice the "
                                               "handpainted ceiling fresco.")]
INVALID = ["", ""]

GAME_MAP = [[KITCHEN,      CORRIDOR, GALLERY,  CORRIDOR, ARBORETUM],
            [CORRIDOR,     INVALID,  CORRIDOR, INVALID,  CORRIDOR],
            [FREEZER,      CORRIDOR, ROTUNDA,  CORRIDOR, LIBRARY],
            [CORRIDOR,     INVALID,  CORRIDOR, INVALID,  CORRIDOR],
            [BROOM_CLOSET, CORRIDOR, DISCO,    CORRIDOR, BATHROOM]]


class Player:
    def __init__(self):
        self.key = False
        self.hat = False
        self.bunny = False
        self.ring = False
        self.box = False
        self.comb = False
        self.disco_ground_score = False
        self.first_library_book = True
        self.first_ghost_fight = True
        self.proton_pack_charge = 3
        self.x = 2
        self.y = 2

    def new_room(self):
        room = GAME_MAP[self.y][self.x][0]
        room_intro = GAME_MAP[self.y][self.x][1]
        return room, room_intro


def print_pause(text_to_print):
    print(text_to_print)
    time.sleep(TIME_SPEED)


def intro():
    print_pause("Welcome to Ghostbusters: The Game!")
    print_pause("*cue theme song*")
    print_pause("Henry Kissinger has been having a ghastly problem:")
    print_pause("His lavish D.C. estate is currently being haunted "
                "by the ghost of Robert McNamara.")
    print_pause("It's your job to explore the main floor of his mansion "
                "and rid the grounds of McNamera's ghost once and for all.")
    print_pause("Your proton pack only has enough charge for three capture "
                "attempts, so take proper aim and good luck!")
    print_pause("The butler shows you to the rotunda, where the most "
                "recent ghost-sighting happened earlier this week.")


def play_game():
    player = Player()
    intro()

    while True:
        (player.x, player.y) = move_player(player, ("Please enter a direction "
                                                    "to move in.\n"))

        room, room_intro = player.new_room()
        print_pause(f"You have entered {room}.")
        print_pause(room_intro)
        if not room_is_interactive(player):
            continue
        else:
            room_is_interactive(player)


def move_player(player, prompt):
    move_response = input(prompt).lower()
    if move_response in list_of_valid_cardinal_directions:
        return check_move_validity(player, move_response)
    else:
        return move_player(player, ("Please enter a cardinal direction "
                                    "(ex. 'n', 's', 'e, 'w'.)\n"))


def check_move_validity(player, move_response):
    (new_x, new_y) = apply_direction(player, move_response)

    if new_y > 4 or new_x > 4 or new_y < 0 or\
       new_x < 0 or GAME_MAP[new_y][new_x] == INVALID:
        print_pause("There doesn't appear to be a way out here.")
        return move_player(player, ("Please select another "
                                    "direction to move in.\n"))
    else:
        return (new_x, new_y)


def apply_direction(player, direction):
    if direction == NORTH:
        return (player.x, player.y - 1)
    if direction == SOUTH:
        return (player.x, player.y + 1)
    if direction == EAST:
        return (player.x + 1, player.y)
    if direction == WEST:
        return (player.x - 1, player.y)


def room_is_interactive(player):
    if GAME_MAP[player.y][player.x] == GALLERY:
        return open_locks(player)
    elif GAME_MAP[player.y][player.x] == DISCO:
        return disco(player)
    elif GAME_MAP[player.y][player.x] == BATHROOM:
        return bathroom(player)
    elif GAME_MAP[player.y][player.x] == LIBRARY:
        return library(player)
    elif GAME_MAP[player.y][player.x] == FREEZER:
        return freezer(player)
    else:
        return False


def yes_no_response(prompt):
    response = input(prompt)
    if response.lower() in YES_RESPONSE:
        return True
    elif response.lower() in NO_RESPONSE:
        return False
    else:
        return yes_no_response("Sorry, I don't understand. Please respond "
                               "with 'yes' or 'no'.\n")


def coin_flip():
    return random.choice([True, False])


def disco(player):
    answer = yes_no_response("Would you like to scan the room for ground"
                             "scores?\n")
    if answer and not player.disco_ground_score:
        print_pause("While rummaging through the fallen streamers and party "
                    "cups, you manage to find an unopened package "
                    "of Skittles and a sweet party hat.")
        if yes_no_response("Would you like to pick these up?\n"):
            print_pause("You put the hat on and tuck the Skittles "
                        "into your back pocket for later.")
            player.disco_ground_score = True
            player.hat = True
    elif answer and player.disco_ground_score:
        print_pause("There doesn't appear to be anything else "
                    "interesting here.")
        print_pause("Your shoes are noticably sticker now.")
    return


def bathroom(player):
    print_pause("Above the toilet are giant ebony cabinets, with "
                "large ivory handles.")
    if yes_no_response("Would you care to take a peek inside?\n"):
        if (player.bunny and
           player.key and
           player.ring and
           player.box and
           player.comb):
            print_pause("Haven't you ransacked this place enough??")
        elif (player.bunny and
              player.key and
              player.ring and
              player.box and
              not player.comb):
            print_pause("The inside of the cabinet is mostly bare, except "
                        "for an ornate tortoise shell comb.")
            if yes_no_response("I bet you'd like to steal that too, wouldn't "
                               "you, you dirty thief?\n"):
                print_pause("You give your hair a quick run through "
                            "and add the comb to your Kissinger "
                            "memorabilia collection.")
                player.comb = True
        elif not player.box:
            print_pause("The inside of the cabinet is mostly bare, "
                        "except for an ornate tortoise shell "
                        "comb and small jewelry box.")
            if yes_no_response("Would you like to open the jewelry box?\n"):
                if player.bunny and
                player.key and
                player.ring:
                    print_pause("There's nothing interesting about an "
                                "empty box...")
                    if yes_no_response("...unless you'd like to take that "
                                       "as well?\n"):
                        print_pause("Unbelievable. This game really caters "
                                    "to the morally depraved, doesn't it?")
                        print_pause("As you reach for the jewelry box, a "
                                    "loud clatter in the hallway startles "
                                    "and distracts you.")
                        print_pause("When you turn back around, the box is "
                                    "GONE.")
                        print_pause("Back to work, Ghostbuster!")
                        player.box = True
                else:
                    print_pause("You peer inside of the jewelry box "
                                "to discover a large diamond ring, "
                                "an ornate brass key, and a dust bunny.")
                    if yes_no_response("Would you like to pick "
                                       "any of these up?\n"):
                        pick_up_items(player)


def pick_up_question(player):
    if yes_no_response("Would you like to pick anything else up?\n"):
        return pick_up_items(player)


def pick_up_items(player):
    pick_up = input("Please type 'bunny', 'ring', or 'key' "
                    "to pick up an item.\n")
    if pick_up == "bunny":
        if player.bunny:
            print_pause("The bunny is long gone! Hop to it if you want "
                        "to catch that little rascal.")
        else:
            print_pause("You reach for the bunny, but it hops out of the "
                        "box and scampers off down the hallway.")
            player.bunny = True
        pick_up_question(player)
    elif pick_up == "ring":
        if player.ring:
            print_pause("You frantically rummage through your pocket "
                        "for the ring, wrapping your fingers "
                        "around its smooth diamond.")
        else:
            print_pause("You dust off the ring and hurridly pocket it, "
                        "hoping no one noticed.")
            player.ring = True
        pick_up_question(player)
    elif pick_up == "key":
        if player.key:
            print_pause("Better figure out what your key goes to "
                        "before you go looking for another.")
        else:
            print_pause("The key doesn't match the lock on the jewelry "
                        "box, so you put it in your pocket, "
                        "in case it proves useful later.")
            player.key = True
        pick_up_question(player)
    else:
        print_pause("Sorry, I don't understand.")
        pick_up_items(player)


def library(player):
    if player.first_library_book:
        player.first_library_book = False
        book_choice(player, yes_no_response("Would you like to choose "
                                            "a book? \n"))
    else:
        book_choice(player, yes_no_response("Would you like to choose "
                                            "another book?\n"))


def book_choice(player, answer):
    if answer:
        book_list = [["You select a dusty copy of the Canterbury Tales.",
                      "Sadly, moths have eaten away most of the pages, "
                      "and the book falls apart in your hands."],
                     ["You select a first-edition copy of 'How to Succeed "
                      "in Business Without Really Trying'",
                      "It appears to be autographed, but you can't tell if "
                      "the signature belongs to the author or owner."],
                     ["You select an old copy of the Holy Bible.",
                      "Upon opening it, you discover that the pages have "
                      "been cut out to make room for a whiskey flask."],
                     ["You select a copy of 'Hogwarts: A History'",
                      "Suddenly, a book across the room falls off "
                      "its shelf and crashes to the floor."]]

        book_select = random.randint(0, 3)
        print_pause(book_list[book_select][0])
        print_pause(book_list[book_select][1])
        if book_select == 3:
            if yes_no_response("Would you like to go investigate?\n"):
                print_pause("You cross the room to retrieve the fallen book.")
                print_pause("The cover and pages of the book "
                            "are all completely blank!")
                print_pause("As you peer up at the shelf the book fell from, "
                            "you notice that the entire shelf is full of "
                            "these blank volumes.")
                print_pause("While odd, this seems to have "
                            "no particular significance.")
        library(player)
    else:
        player.first_library_book = True


def freezer(player):
    print_pause("Your charge depletes by one battery cell!")
    player.proton_pack_charge -= 1
    if player.proton_pack_charge == 2:
        print_pause("This leaves you two more chances to catch the ghost.")
    elif player.proton_pack_charge == 1:
        print_pause("You only have one more chance to catch the ghost!")
    elif player.proton_pack_charge == 0:
        game_over(False)


def open_locks(player):
    if yes_no_response("Would you like to try any of the locks?\n"):
        if player.key:
            print_pause("You try a few of the locks, to no avail...")
            print_pause("But wait...the key seems to fit into the door of "
                        "the old wardrobe in the corner.")
            print_pause("You turn the key and remove the "
                        "padlock when suddenly...")
            print_pause('OUT POPS A GHOST! "OOOOOOOOOOOO", the old warmonger '
                        "shouts, as he violently crashes about the room, "
                        "waving his arms in sheer terror.")
            if player.hat:
                print_pause('"I see you stole my hat, you conniving thief! "'
                            "You'll pay for this!")
            ghost_fight_attempt(player)
        else:
            print_pause("All of the locks are locked. "
                        "Perhaps there's a key around here somewhere...")


def ghost_fight_attempt(player):
    print_pause("Now's your chance to rid the world of "
                "McNamara once and for all!")
    if player.first_ghost_fight:
        ghost_fight_text = "Would you like to try to capture the ghost?\n"
    else:
        ghost_fight_text = "Would you like to try again?\n"

    if yes_no_response(ghost_fight_text):
        ghost_battle(player)
    else:
        print_pause("What are you waiting for?! Who knows "
                    "when the ghost might appear again.")
        player.first_ghost_fight = True


def ghost_battle(player):
    print_pause("You take aim and fire your proton pack at the ghost.")
    player.proton_pack_charge -= 1
    player.first_ghost_fight = False

    if coin_flip():
        print_pause("SUCCESS!")
        print_pause("After an intense few minutes, you manage to trap "
                    "the ghost and complete your mission!")
        game_over(True)
    else:
        if player.proton_pack_charge != 0:
            print_pause("Damn! The ghost escapes the beam of your proton "
                        "pack and is even more irritated.")
            print_pause("He begins to taunt you mercilessly.")
            ghost_fight_attempt(player)
        else:
            print_pause("Your aim isn't so great, and "
                        "the ghost manages to escape!")
            game_over(False)


def game_over(result):
    if not result:
        print_pause("Unfortunately, your proton pack battery is now dead.")
        print_pause("Mr. Kissinger demands a refund.")
        print_pause("The final score for this round:")
        print_pause("Ghosts - 1")
        print_pause("Ghostbusters - 0")
    else:
        print_pause("Congratulations on your victory!")
        print_pause("Now it's time for you to purchase the second "
                    "installment in this series, 'Ghostbusters 2 - Invoice':")
        print_pause("a zany journey through time and space to track down "
                    "Henry Kissinger and obtain payment for your services.")
    print_pause("GAME OVER")

    if yes_no_response("Would you like to play again?\n"):
        play_game()
    else:
        exit()


play_game()
