class Session:
    def __init__(self, id, session_date, cards_studied, new_cards, accurate_rate):
        self.id = id
        self.session_date = session_date
        self.cards_studied = cards_studied
        self.new_cards = new_cards
        self.accurate_rate = accurate_rate
