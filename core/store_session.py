from models.database import Database


def store_session(cards_studied, new_cards, accurate_rate):
    db = Database()
    db.store_session(cards_studied, new_cards, accurate_rate)
