#home AI
import reading_book as bookAI

def home(self, user):
    print(f"Hello {user}! I am your personal AI assistant. How can I help you today?")
    print("1. Reading Book")
    print("2. Motivation")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        bookAI.main()
    elif choice == "2":
        import motivation
        motivation.keep_motivated()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice. Please try again.")
        home(user)
