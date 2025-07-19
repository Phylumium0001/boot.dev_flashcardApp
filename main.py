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


def calc_stats(sessions -> List):
    cram_num = 0
    new_num = 0
    due_num = 0
    mixed_num = 0

    max_accuracy = 1
    min_accuracy = 0

    total_card_num = 0

    for session in sessions -> Tuple:
        id, session_type, session_date,
        cards_studied, new_cards,
        accuracy = session

        if session_type == "Cram Session":
            cram_num += 1
        elif session_type == "New Cards Session"
        new_num += 1


def show_player_stats():
    db = Database()

    sessions = db.get_all_sessions()
    num_session = len(sessions)

    print(f"""
    User Name :
    Total Sessions : {num_session}
    New Cards Mode : {new_num}
    Due Cards Mode : {due_num}
    Cram Mode : {cram_num}
    Mixed Mode : {mixed_num}
    """)
    return


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
