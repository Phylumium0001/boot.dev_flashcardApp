from typing import List
from core import study_session
from models.database import Database


def handle_study_sessions():
    studySession = input(
        """
    Cards
    New - 0  Due - 0

    Select Your Session :

    [1] - New Cards Introductions
    [2] - Review Due Cards
    [3] - Cram Mode (Intensive Session)
    [4] - Mixed Mode

    ((Q)uit App)
    >> """)

    if studySession == "1":
        print("Reviewing New Cards")
        # load_session_new_cards()
        study_session.review_new_cards()

    elif studySession == "2":
        print("Reviewing Due Cards")
        # load_session_due_cards()
        study_session.review_due_cards()

    elif studySession == "3":
        print("Cram Session")
        # load_session_cram()
        study_session.cram_session()

    elif studySession == "4":
        print("Mixed Session")
        # load_session_mixed()
        study_session.mixed_session()

    elif studySession.upper() == "Q":
        print("Good Bye")
        return "Exit"

    else:
        print("Enter a Valid input")


def calc_stats(sessions: List):
    cram_num = 0
    new_num = 0
    due_num = 0
    mixed_num = 0

    max_accuracy = 1
    min_accuracy = 0

    first_session = True

    for session in sessions:
        id, session_type, session_date, cards_studied, new_cards, accuracy = session

        if session_type == "Cram Session":
            cram_num += 1
        elif session_type == "New Cards Session":
            new_num += 1
        elif session_type == "Due Cards Session":
            due_num += 1
        elif session_type == "Mixed Cards Session":
            mixed_num += 1

        if first_session:
            max_accuracy = accuracy
            min_accuracy = accuracy
            first_session = False
        else:
            if accuracy > max_accuracy:
                max_accuracy = accuracy
            if accuracy < min_accuracy:
                min_accuracy = accuracy

    return {
        "cram_sessions": cram_num,
        "new_sessions": new_num,
        "due_sessions": due_num,
        "mixed_sessions": mixed_num,
        "max_accuracy": max_accuracy,
        "min_accuracy": min_accuracy,
    }


def show_player_stats():
    db = Database()

    sessions = db.get_all_sessions()
    stats = calc_stats(sessions)
    stats['total_cards_number'] = len(sessions)
    stats['average_accuracy'] = (stats['min_accuracy']+stats['max_accuracy'])/2

    print(f"""
    User Name :
    Total Sessions   : {stats['total_cards_number']}
    New Cards Mode   : {stats['new_sessions']}
    Due Cards Mode   : {stats['due_sessions']}
    Cram Mode        : {stats['cram_sessions']}
    Mixed Mode       : {stats['mixed_sessions']}

    Maximum accuracy : {stats['max_accuracy'] * 100}%
    Minimum accuracy : {stats['min_accuracy'] * 100}%
    Average accuracy : {stats['average_accuracy'] * 100}%
    """)


def main():
    # Load Cards
    print("Welcome, to Vocabs App")
    while True:
        mode = input("""
        [1] - Player Statistics
        [2] - Begin Session
        """)
        if mode not in ['1', '2', 'q']:
            print("Invalid Input. Try Again.\n")
            continue
        if mode == '1':
            show_player_stats()
        elif mode == '2':
            handle_study_sessions()
        else:
            break


if __name__ == "__main__":
    main()
