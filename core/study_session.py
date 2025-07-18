from datetime import datetime

from models.database import Database
from models.card import Card
from core.space_repitition import calculate_next_review
from core.store_session import store_session


def run_session(cards, cram_mode=False):
    """
    Handles Showing the cards
    """
    db = Database()

    reviewed_cards = 0
    correct_response = 0
    new_card_num = 0

    res_map = {0: 'easy', 1: "good", 2: "hard", 3: "again"}
    if cram_mode:
        for card in cards:
            print(card.arabic_word)
            response = input("Q-Quit 0-Easy 1-Good 2-Hard 3-Again >> ")
            if response not in ['q', 'Q', '0', '1', '2', '3']:
                print("Ending Session Prematurely. Session not saved")
                return

            # Correct Response(User remmembered)
            if response in ['1', '2']:
                correct_response += 1

            if card.card_state == "new":
                new_card_num += 1

            reviewed_cards += 1

        accurate_rate = correct_response / reviewed_cards
        store_session(reviewed_cards, new_card_num, accurate_rate)

        return

    for card in cards:
        print(card.arabic_word)
        response = int(input("0-Easy 1-Good 2-Hard 3-Again >> "))
        # Get new interval
        new_card = calculate_next_review(card, res_map[response])

        # Update the repititions
        new_card.repititions += 1

        # Update the last reviewed
        new_card.last_review = datetime.now()

        # Update card state
        if (new_card.card_state == "new"):
            new_card_num += 1
            new_card.card_state = "learning"

        db.update_card(new_card)

        # Correct Response(User remmembered)
        if response in ['1', '2']:
            correct_response += 1

        reviewed_cards += 1

    accurate_rate = correct_response / reviewed_cards

    store_session(reviewed_cards, new_card_num, accurate_rate)

    print("Well Done!!!")


def gen_card_objs(data):
    card_objs = []
    for datum in data:
        card_objs.append(Card._from_tuple(datum))

    return card_objs


def review_new_cards():
    """
    Review all new cards only
    """
    db = Database()
    # Get all new cards
    cards = db.get_new_cards()

    # Cards present
    if len(cards) > 0:
        # Create card objects
        card_objs = gen_card_objs(cards)

        # Run session
        run_session(card_objs)

    else:
        print("No new cards")


def review_due_cards():
    """
    Review all the cards that have passed their review date
    """

    db = Database()
    # Get all new cards
    cards = db.get_due_cards()

    # Cards present
    if len(cards) > 0:
        # Create card objects
        card_objs = gen_card_objs(cards)

        # Run session
        run_session(card_objs)

    else:
        print("No due cards")


def cram_session():
    """
    Crams a larger number of words for revision
    Does not affect review date
    """
    db = Database()
    # Get all new cards
    cards = db.get_learning_cards(limit=5)
    print(cards)

    # Cards present
    if len(cards) > 0:
        # Create card objects
        card_objs = gen_card_objs(cards)

        # Run session
        run_session(card_objs, cram_mode=True)

    else:
        print("No new cards")


def mixed_session():
    """
    Mixes new and learning cards
    """
    db = Database()
    # Get all new cards
    new_cards = db.get_new_cards()
    old_cards = db.get_learning_cards(10)

    cards = new_cards + old_cards
    # Cards present
    if len(cards) > 0:
        # Create card objects
        card_objs = gen_card_objs(cards)

        # Run session
        run_session(card_objs, cram_mode=True)

    else:
        print("No cards found")
