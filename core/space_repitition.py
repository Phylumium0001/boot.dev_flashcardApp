from datetime import datetime, timedelta


def calculate_next_review(card, response):
    if response == "again":
        card.ease_factor -= 0.20
        card.interval_days = 1
    elif response == "hard":
        card.ease_factor -= 0.15
        card.interval_days = max(1, card.interval_days * 1.2)
    elif response == "good":
        card.interval_days = card.interval_days * card.ease_factor
    elif response == "easy":
        card.ease_factor += 0.15
        card.interval_days = card.interval_days * card.ease_factor * 1.3

    # Ensure minimum ease factor
    card.ease_factor = max(1.3, card.ease_factor)

    # Schedule next review
    card.next_review = datetime.now().date() + timedelta(card.interval_days)

    return card
