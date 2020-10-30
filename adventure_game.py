import time
import random

TIME_SPEED = .2

DEFAULT_PROMPT = "Please enter a direction to move in.\n"

list_of_valid_cardinal_directions = ["n", "s", "e", "w"]

NORTH = "n"
SOUTH = "s"
EAST = "e"
WEST = "w"

YES_RESPONSE = ["yes", "y", "yep"]
NO_RESPONSE = ["no", "n", "nope"]

HAT = "hat"
KEY = "key"
BUNNY = "bunny"
RING = "ring"
BOX = "box"
COMB = "comb"

proton_pack_charge = 3
proton_pack_charge_reset = 3
library_question_index = 0
library_question_index_reset = 0
disco_ground_score_index = 0
disco_ground_score_index_reset = 0
ghost_fight_index = 0
ghost_fight_index_reset = 0
items = []
items_reset = []

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

game_map = [[KITCHEN,      CORRIDOR, GALLERY,  CORRIDOR, ARBORETUM],
            [CORRIDOR,     INVALID,  CORRIDOR, INVALID,  CORRIDOR],
            [FREEZER,      CORRIDOR, ROTUNDA,  CORRIDOR, LIBRARY],
            [CORRIDOR,     INVALID,  CORRIDOR, INVALID,  CORRIDOR],
            [BROOM_CLOSET, CORRIDOR, DISCO,    CORRIDOR, BATHROOM]]

x_coor = 2
y_coor = 2
start_position = game_map[y_coor][x_coor]


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
    intro()
    get_move_response(y_coor, x_coor, DEFAULT_PROMPT)


def get_move_response(y_coor, x_coor, prompt):
    move_response = input(prompt).lower()
    if move_response in list_of_valid_cardinal_directions:
        check_validity(y_coor, x_coor, move_response)
    else:
        response_try_again = "Please enter a cardinal direction "\
                             "(ex. 'n', 's', 'e, 'w'.)\n")
        get_move_response(y_coor, x_coor, response_try_again)


def check_validity(y_coor, x_coor, move_response):
    (new_y_coor, new_x_coor) = apply_direction(y_coor, x_coor, move_response)
    if invalid_move(new_y_coor, new_x_coor):
        invalid_move_response(y_coor, x_coor)
    else:
        move(new_y_coor, new_x_coor)


def apply_direction(y_coor, x_coor, direction):
    if direction == NORTH:
        return (y_coor - 1, x_coor)
    if direction == SOUTH:
        return (y_coor + 1, x_coor)
    if direction == EAST:
        return (y_coor, x_coor + 1)
    if direction == WEST:
        return (y_coor, x_coor - 1)


def invalid_move(new_y_coor, new_x_coor):
    if new_y_coor > 4 or new_x_coor > 4 or new_y_coor < 0 or\
       new_x_coor < 0 or game_map[new_y_coor][new_x_coor] == INVALID:
        return True


def invalid_move_response(y_coor, x_coor):
    print_pause("There doesn't appear to be a way out here.")
    get_move_response(y_coor, x_coor, ("Please select another "
                                       "direction to move in.\n"))


def move(y_coor, x_coor):
    room = game_map[y_coor][x_coor][0]
    room_intro = game_map[y_coor][x_coor][1]
    new_room(y_coor, x_coor, room, room_intro)


def new_room(y_coor, x_coor, room, room_intro):
    print_pause(f"You have entered {room}.")
    print_pause(room_intro)
    is_room_interactive(y_coor, x_coor)


def is_room_interactive(y_coor, x_coor):
    if game_map[y_coor][x_coor] == GALLERY:
        gallery_lock_prompt()
    elif game_map[y_coor][x_coor] == DISCO:
        disco()
    elif game_map[y_coor][x_coor] == BATHROOM:
        bathroom()
    elif game_map[y_coor][x_coor] == LIBRARY:
        library()
    elif game_map[y_coor][x_coor] == FREEZER:
        freezer()
    get_move_response(y_coor, x_coor, DEFAULT_PROMPT)


def yes_no_question(response):
    if response.lower() in YES_RESPONSE:
        return "y"
    if response.lower() in NO_RESPONSE:
        return "n"
    else:
        try_again = input("Sorry, I don't understand. Please respond "
                          "with 'yes' or 'no'.\n")
        return yes_no_question(try_again)


def coin_flip():
    flip = random.randint(0, 1)
    if flip == 0:
        return "y"
    if flip == 1:
        return "n"


def gallery_lock_prompt():
    first_lock = input("Would you like to try any of the locks?\n")
    answer = yes_no_question(first_lock)
    if answer == "y":
        open_locks()


def open_locks():
    if KEY in items:
        print_pause("You try a few of the locks, to no avail...")
        print_pause("But wait...the key seems to fit into the door of "
                    "the old wardrobe in the corner.")
        print_pause("You turn the key and remove the "
                    "padlock when suddenly...")
        print_pause('OUT POPS A GHOST! "OOOOOOOOOOOO", the old warmonger '
                    "shouts, as he violently crashes about the room, waving "
                    "his arms in sheer terror.")
        if HAT in items:
            print_pause('"I see you stole my hat, you conniving thief! "'
                        "You'll pay for this!")
        ghost_fight_setup()
    else:
        print_pause("All of the locks are locked. "
                    "Perhaps there's a key around here somewhere...")


def disco():
    global disco_ground_score_index
    scan_floor = input("Would you like to scan the room for ground scores?\n")
    answer = yes_no_question(scan_floor)
    if answer == "y" and disco_ground_score_index == 0:
        print_pause("While rummaging through the fallen streamers and party "
                    "cups, you manage to find an unopened package "
                    "of Skittles and a sweet party hat.")
        pick_up = input("Would you like to pick these up?\n")
        answer = yes_no_question(pick_up)
        if answer == "y":
            print_pause("You put the hat on and tuck the Skittles "
                        "into your back pocket for later.")
            disco_ground_score_index = 1
            items.append(HAT)
    elif answer == "y" and disco_ground_score_index == 1:
        print_pause("There doesn't appear to be anything else "
                    "interesting here.")
        print_pause("Your shoes are noticably sticker now.")


def bathroom():
    print_pause("Above the toilet are giant ebony cabinets, with "
                "large ivory handles.")
    open_drawers = input("Would you care to take a peek inside?\n")
    answer = yes_no_question(open_drawers)
    if answer == "y":
        if (BUNNY and KEY and RING and BOX and COMB) in items:
            print_pause("Haven't you ransacked this place enough??")
        elif (BUNNY and KEY and RING and BOX) in items:
            print_pause("The inside of the cabinet is mostly bare, except "
                        "for an ornate tortoise shell comb.")
            steal_comb = input("I bet you'd like to steal that too, wouldn't "
                               "you, you dirty thief?\n")
            answer = yes_no_question(steal_comb)
            if answer == "y":
                print_pause("You give your hair a quick run through "
                            "and add the comb to your Kissinger "
                            "memorabilia collection.")
                items.append(COMB)
        else:
            print_pause("The inside of the cabinet is mostly bare, "
                        "except for an ornate tortoise shell "
                        "comb and small jewelry box.")
            open_box = input("Would you like to open the jewelry box?\n")
            answer = yes_no_question(open_box)
            if answer == "y":
                if (BUNNY in items) and (KEY in items) and (RING in items):
                    all_items_retrieved()
                else:
                    print_pause("You peer inside of the jewelry box "
                                "to discover a large diamond ring, "
                                "an ornate brass key, and a dust bunny.")
                    pick_up_prompt = input("Would you like to pick "
                                           "any of these up?\n")
                    answer = yes_no_question(pick_up_prompt)
                    print(answer)
                    if answer == "y":
                        all_items_retrieved()


def pick_up_question():
    question = input("Would you like to pick anything else up?\n")
    answer = yes_no_question(question)
    if answer == "y":
        all_items_retrieved()


def all_items_retrieved():
    if (BUNNY in items) and (KEY in items) and (RING in items):
        print_pause("There's nothing interesting about an enpty box...")
        take_box = input("...unless you'd like to take that as well?\n")
        answer = yes_no_question(take_box)
        if answer == "y":
            print_pause("Unbelievable. This game really caters to the "
                        "morally depraved, doesn't it?")
            print_pause("As you reach for the jewelry box, a loud clatter "
                        "in the hallway startles and distracts you.")
            print_pause("When you turn back around, the box is GONE.")
            print_pause("Back to work, Ghostbuster!")
            items.append(BOX)
    else:
        pick_up_items()


def pick_up_items():
    pick_up = input("Please type 'bunny', 'ring', or 'key' "
                    "to pick up an item.\n")
    if pick_up == "bunny":
        if BUNNY in items:
            print_pause("The bunny is long gone! Hop to it if you want "
                        "to catch that little rascal.")
        else:
            print_pause("You reach for the bunny, but it hops out of the "
                        "box and scampers off down the hallway.")
            items.append(BUNNY)
        pick_up_question()
    elif pick_up == "ring":
        if RING in items:
            print_pause("You frantically rummage through your pocket "
                        "for the ring, wrapping your fingers "
                        "around the smooth diamond.")
        else:
            print_pause("You dust off the ring and hurridly pocket it, "
                        "hoping no one noticed.")
            items.append(RING)
        pick_up_question()
    elif pick_up == "key":
        if KEY in items:
            print_pause("Better figure out what your key goes to "
                        "before you go looking for another.")
        else:
            print_pause("The key doesn't match the lock on the jewelry "
                        "box, so you put it in your pocket, "
                        "in case it proves useful later.")
            items.append(KEY)
        pick_up_question()
    else:
        print_pause("Sorry, I don't understand.")
        pick_up_items()


def library():
    global library_question_index
    if library_question_index == 0:
        library_question_index += 1
        choose_book = input("Would you like to choose a book?\n")
        answer = yes_no_question(choose_book)
        book_choice(answer)
    else:
        choose_book = input("Would you like to choose another book?\n")
        answer = yes_no_question(choose_book)
        book_choice(answer)


def book_choice(answer):
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
    if answer == "y":
        book_select = random.randint(0, 3)
        print_pause(book_list[book_select][0])
        print_pause(book_list[book_select][1])
        if book_select == 3:
            hogwarts_book()
        else:
            library()
    else:
        global library_question_index
        library_question_index = 0


def hogwarts_book():
    investigate = input("Would you like to go investigate?\n")
    answer = yes_no_question(investigate)
    if answer == "y":
        print_pause("You cross the room to retrieve the fallen book.")
        print_pause("The cover and pages of the book "
                    "are all completely blank!")
        print_pause("As you peer up at the shelf the book fell from, "
                    "you notice that the entire shelf is full of "
                    "these blank volumes.")
        print_pause("While odd, this seems to have "
                    "no particular significance.")
    library()


def freezer():
    print_pause("Your charge depletes by one battery cell!")
    global proton_pack_charge
    proton_pack_charge -= 1
    if proton_pack_charge == 2:
        print_pause("This leaves you two more chances to catch the ghost.")
    if proton_pack_charge == 1:
        print_pause("You only have one more chance to catch the ghost!")
    if proton_pack_charge == 0:
        game_over(False)


def ghost_fight_setup():
    print_pause("Now's your chance to rid the world of "
                "McNamara once and for all!")
    ghost_fight_text()


def ghost_fight_text():
    global ghost_fight_index
    if ghost_fight_index == 0:
        ghost_fight_text = "Would you like to try to capture the ghost?\n"
    else:
        ghost_fight_text = "Would you like to try again?\n"
    ghost_fight_confirm(ghost_fight_text)


def ghost_fight_confirm(ghost_fight_text):
    global ghost_fight_index
    global proton_pack_charge
    capture_attempt = input(ghost_fight_text)
    answer = yes_no_question(capture_attempt)
    if answer == "y":
        print_pause("You take aim and fire your proton pack at the ghost.")
        proton_pack_charge -= 1
        ghost_fight_index = 1
        ghost_battle()
    else:
        print_pause("What are you waiting for?! Who knows "
                    "when the ghost might appear again.")
        ghost_fight_index = 0


def ghost_battle():
    global ghost_fight_index
    answer = coin_flip()
    if answer == "y":
        print_pause("SUCCESS!")
        print_pause("After an intense few minutes, you manage to trap "
                    "the ghost and complete your mission!")
        game_over(True)
    else:
        failed_ghost_battle()


def failed_ghost_battle():
    if proton_pack_charge != 0:
        print_pause("Damn! The ghost escapes the beam of your proton "
                    "pack and is even more irritated.")
        print_pause("He begins to taunt you mercilessly.")
        ghost_fight_text()
    else:
        print_pause("Your aim isn't so great, and "
                    "the ghost manages to escape!")
        game_over(False)


def reset_game():
    global items
    items = items_reset
    global proton_pack_charge
    proton_pack_charge = proton_pack_charge_reset
    global disco_ground_score_index
    disco_ground_score_index = disco_ground_score_index_reset
    global library_question_index
    library_question_index = library_question_index_reset
    global ghost_fight_index
    ghost_fight_index = ghost_fight_index_reset
    play_game()


def game_over(result):
    global proton_pack_charge
    if result is False:
        print_pause("Unfortunately, your proton pack battery is now dead.")
        print_pause("Mr. Kissinger demands a refund.")
        print_pause("The final score for this round:")
        print_pause("Ghosts - 1")
        print_pause("Ghostbusters - 0")
    else:
        print_pause("Congratulations on your victory!")
        print_pause("Now it's time for you to purchase the second "
                    "installment in this series, 'Ghostbusters: Invoice':")
        print_pause("a zany journey through time and space to track down "
                    "Henry Kissinger and obtain payment for your services.")
    print_pause("GAME OVER")
    replay = input("Would you like to play again?\n")
    answer = yes_no_question(replay)
    if answer == "y":
        reset_game()
    else:
        exit()


play_game()
