from models.database import Database
from models.card import Card
from core.space_repitition import calculate_next_review
import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        # Clean up any existing test data
        self.db.c.execute("DELETE FROM cards")
        self.db.conn.commit()

    def test_add_card(self):
        self.db.add_card("مرحبا", "hello")
        cards = self.db.get_new_cards()
        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0][1], "مرحبا")
        self.assertEqual(cards[0][2], "hello")

    def test_get_new_cards(self):
        self.db.add_card("كتاب", "book")
        self.db.add_card("قلم", "pen")
        cards = self.db.get_new_cards()
        self.assertEqual(len(cards), 2)

    def test_update_card(self):
        self.db.add_card("بيت", "house")
        cards = self.db.get_new_cards()
        card = Card._from_tuple(cards[0])
        card.interval_days = 5
        card.ease_factor = 2.8
        self.db.update_card(card)
        # Note: This test would need a get_card_by_id method to properly verify


class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card_data = (1, "سيارة", "car", 2.5, 1, 0, None, None, None, "new")
        card = Card._from_tuple(card_data)
        self.assertEqual(card.id, 1)
        self.assertEqual(card.arabic_word, "سيارة")
        self.assertEqual(card.translation, "car")
        self.assertEqual(card.ease_factor, 2.5)
        self.assertEqual(card.interval_days, 1)
        self.assertEqual(card.card_state, "new")

    def test_card_repr(self):
        card_data = (1, "ماء", "water", 2.5, 1, 0, None, None, None, "new")
        card = Card._from_tuple(card_data)
        expected = "CARD : ماء --> water\nE : 2.5, I : 1"
        self.assertEqual(repr(card), expected)


class TestSpacedRepetition(unittest.TestCase):
    def setUp(self):
        card_data = (1, "شمس", "sun", 2.5, 1, 0, None, None, None, "new")
        self.card = Card._from_tuple(card_data)

    def test_again_response(self):
        original_ease = self.card.ease_factor
        calculate_next_review(self.card, "again")
        self.assertEqual(self.card.interval_days, 1)
        self.assertEqual(self.card.ease_factor, original_ease - 0.20)

    def test_hard_response(self):
        original_ease = self.card.ease_factor
        original_interval = self.card.interval_days
        calculate_next_review(self.card, "hard")
        self.assertEqual(self.card.ease_factor, original_ease - 0.15)
        self.assertEqual(self.card.interval_days,
                         max(1, original_interval * 1.2))

    def test_good_response(self):
        original_ease = self.card.ease_factor
        original_interval = self.card.interval_days
        calculate_next_review(self.card, "good")
        self.assertEqual(self.card.interval_days,
                         original_interval * original_ease)
        self.assertEqual(self.card.ease_factor, original_ease)

    def test_easy_response(self):
        original_ease = self.card.ease_factor
        original_interval = self.card.interval_days
        calculate_next_review(self.card, "easy")
        self.assertEqual(self.card.ease_factor, original_ease + 0.15)
        self.assertEqual(self.card.interval_days,
                         original_interval * (original_ease + 0.15) * 1.3)

    def test_minimum_ease_factor(self):
        # Set ease factor very low and test "again" response
        self.card.ease_factor = 1.4
        calculate_next_review(self.card, "again")
        self.assertEqual(self.card.ease_factor, 1.3)  # Should not go below 1.3

    def test_next_review_date_set(self):
        self.assertIsNone(self.card.next_review)
        calculate_next_review(self.card, "good")
        self.assertIsNotNone(self.card.next_review)


if __name__ == '__main__':
    unittest.main()
