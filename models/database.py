import sqlite3
import datetime
import asyncio


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("./data/vocabs.db")
        self.c = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            arabic_word TEXT NOT NULL,
            translation TEXT NOT NULL,
            ease_factor REAL DEFAULT 2.5,
            interval_days INTEGER DEFAULT 1,
            repititions INTEGER DEFAULT 0,
            next_review DATETIME DEFAULT (datetime('now')),
            created_at DATETIME DEFAULT (datetime('now')),
            last_review DATETIME DEFAULT NULL,
            card_state TEXT DEFAULT 'new' -- 'new', 'learning', 'review'
        );
        """)

        self.c.execute("""
        CREATE TABLE IF NOT EXISTS study_sessions (
            id PRIMARY KEY NOT NULL,
            session_date DATETIME DEFAULT CURRENT_TIMEZONE,
            cards_studied INTEGER,
            new_cards INTEGER,
            accurate_rate REAL);
        """)

    def add_card(self,
                 arabic_text,
                 translation):
        # Adds a new card to the database
        self.c.execute(f"""INSERT INTO cards
        (arabic_word,translation)
        VALUES (
            '{arabic_text}','{translation}'
        )""")
        self.conn.commit()

    def get_new_cards(self):
        """
        Retrieve all new cards only
        """
        print("Fetching new cards")
        self.c.execute(
            "SELECT * FROM cards WHERE card_state='new' ORDER BY RANDOM() LIMIT 10")
        rows = self.c.fetchall()

        return rows

    def get_due_cards(self):
        """
        Cards which have passed their review date
        """
        self.c.execute("""
        SELECT * FROM cards WHERE next_review < datetime('now') ORDER BY RANDOM() LIMIT 10
        """)
        cards = self.c.fetchall()
        print(cards)
        return cards

    def get_learning_cards(self):
        """
        Cards which have passed their review date
        """
        self.c.execute("""
        SELECT * FROM cards WHERE card_state='learning' ORDER BY RANDOM() LIMIT 20
        """)
        cards = self.c.fetchall()
        return cards

    def update_card(self, card):
        """
        Updates the values of card
        """
        # print("Updating Card")
        # print(card)

        self.c.execute("""
        UPDATE cards
        SET
        arabic_word=?,
        translation=?,
        ease_factor=?,
        interval_days=?,
        repititions=?,
        next_review=?,
        created_at=?,
        last_review=?,
        card_state=?
        WHERE
        id=?
        """, (card.arabic_word, card.translation, card.ease_factor,
              card.interval_days, card.repititions, card.next_review,
              card.created_at, card.last_review, card.card_state, card.id))
        self.conn.commit()


if __name__ == "__main__":
    from card import Card

    db = Database()
    # Generate dummy data to populate the database
    # dummy_cards = [
    #     ('كتاب', 'book'),
    #     ('قلم', 'pen'),
    #     ('بيت', 'house'),
    #     ('سيارة', 'car'),
    #     ('شمس', 'sun'),
    #     ('قمر', 'moon'),
    #     ('ماء', 'water'),
    #     ('طعام', 'food'),
    #     ('مدرسة', 'school'),
    #     ('طالب', 'student'),
    #     ('معلم', 'teacher'),
    #     ('صديق', 'friend'),
    #     ('عائلة', 'family'),
    #     ('يد', 'hand'),
    #     ('عين', 'eye'),
    #     ('أذن', 'ear'),
    #     ('فم', 'mouth'),
    #     ('رأس', 'head'),
    #     ('قدم', 'foot'),
    #     ('قلب', 'heart')
    # ]
    #
    # for arabic_word, translation in dummy_cards:
    #     db.add_card(arabic_word, translation)
    #
    # print(f"Added {len(dummy_cards)} dummy cards to the database")

    # cards = db.get_new_cards()
    # print(cards[0])
    #
    # card1 = Card._from_tuple(cards[0])
    # card1.interval_days = 20
    #
    # db.update_card(card1)
    # db.get_new_cards()

    # print(card1)
    db.get_due_cards()
