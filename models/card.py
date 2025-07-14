import datetime


class Card:
    def __init__(
        self,
        id,
        arabic_word,
        translation,
        ease_factor,
        interval_days,
        repetitions,
        next_review,
        created_at,
        last_review,
        card_state
    ):
        """
        Card Object
        """
        self.id = id
        self.arabic_word = arabic_word
        self.next_review = next_review  # Datetime
        self.created_at = created_at  # Datetime
        self.last_review = last_review  # Datetime
        self.translation = translation
        self.repititions = repetitions
        self.ease_factor = ease_factor
        self.interval_days = interval_days
        self.card_state = card_state

    @classmethod
    def _from_tuple(cls, data):
        return cls(
            data[0], data[1], data[2], data[3],
            data[4], data[5], data[6], data[7],
            data[8], data[9]
        )

    def __repr__(self):
        return f"(Card):ID:{self.id},Arabic:{self.arabic_word},Trans:{self.translation},Ease_f:{self.ease_factor},Interval:{self.interval_days}, card_s:{self.card_state}, next_r:{self.next_review}, last_r:{self.last_review}"
