from models.database import Database


def store_session(session_type, cards_studied, new_cards, accurate_rate):
    db = Database()
    db.store_session(session_type, cards_studied, new_cards, accurate_rate)
