from core import study_session


def main():
    # Load Cards
    print("Welcome, to Vocabs App")
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
    elif studySession == "2":
        print("Reviewing Due Cards")
        # load_session_due_cards()
    elif studySession == "3":
        print("Cram Session")
        # load_session_cram()
    elif studySession == "4":
        print("Mixed Session")
        # load_session_mixed()
    elif studySession.upper() == "Q":
        print("Good Bye")
        return "Exit"
    else:
        print("Enter a Valid input")


if __name__ == "__main__":
    main()
