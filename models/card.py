import datetime


class Card:
    def __init__(
            self,
            arabic,
            next_review_date,
            creation_date,
            last_reviewed,
            translation,
            repition=0,
            ease_factor=2.5,
            interval=1,):
        """
        Card Object
        """
        self.arabic = arabic
        self.next_review_date = next_review_date  # Datetime
        self.creation_date = creation_date  # Datetime
        self.last_reviewed = last_reviewed  # Datetime
        self.translation = translation
        self.repitition = repition
        self.ease_factor = ease_factor
        self.interval = interval
