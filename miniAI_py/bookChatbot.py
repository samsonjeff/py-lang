#OOP book

import difflib
import book_list as libros

class bookChatbot:
    def __init__(self, libros):
        self.book = book
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.book} by {self.author} published in {self.year}'

    def user_feed(self):
        ans = input("How was the book? (good/bad): ").strip().lower()

        if ans in ["good", "yes", "yep", "yeah", "sure", "of course"]:
            print(f'great to hear that you like {self.book} book!')
            self.ask_user()
        elif ans in ["bad", "no", "nope", "nah", "not really", "not sure"]:
            print("Sorry to hear that!")
            user_exit()
        else:
            print("Better to read it first!")
            user_exit()
    
    def readed(self):
        self.user_feed()
        
    def unread(self):
        print(f'I suggest to read {self.book} book its a great book!')
        self.ask_user()

    def ask_user(self):
        ask = input("want to find more book? ").strip().lower()
        if ask in ["yes", "yep", "yeah", "sure", "of course"]:
            return book_chatbot()
        else:
            user_exit()

def book_chatbot():
    book_list = [
        bookChatbot('The Alchemist', 'Paulo Coelho', '1988'),
        bookChatbot('The Power of Now', 'Eckhart Tolle', '1997'),
        bookChatbot('The Subtle Art of Not Giving a F*ck', 'Mark Manson', '2016'),
        bookChatbot('The Four Agreements', 'Don Miguel Ruiz', '1997'),
        bookChatbot('The 48 Laws of Power', 'Robert Greene', '1998'),
    ]

    choose = input('Choose a book: ').strip().lower()
    book_dict = {book.book.lower(): book for book in book_list}
    
    if choose in book_dict:
        selected_book = book_dict[choose]
        print(selected_book)
        readed = input('Have you read the book? (yes/no): ').strip().lower()
        if readed == 'yes':
            selected_book.readed()
        else:
            selected_book.unread()
    else:
        # Predict the closest match
        book_titles = list(book_dict.keys())
        closest_matches = difflib.get_close_matches(choose, book_titles, n=1, cutoff=0.6)
        if closest_matches:
            selected_book = book_dict[closest_matches[0]]
            print(f"Did you mean '{selected_book.book}'?")
            readed = input('Have you read the book? (yes/no): ').strip().lower()
            if readed == 'yes':
                selected_book.readed()
            else:
                selected_book.unread()
        elif choose == 'exit':
            exit()
        else:
            print('Book not found! Here are the available books:')
            for book in book_list:
                print(book)
            return book_chatbot()

def user_exit():
    answer_exit = input("want to end chat? ").strip().lower()
    if answer_exit in ["yes", "yep", "yeah", "sure", "of course"]:
        exit()
    else:
        return book_chatbot()

if __name__ == '__main__':
    book_chatbot()