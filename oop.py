#get the the GWA
import re

class main_for_GWA:

    def __init__ (self, student_name, subject, grade, GWA):
        self.student_name = student_name
        self.subject = subject
        self.grade = grade
        self.GWA = GWA 
        self.subjects_grades = []
    
    def get_all(self): #print out format
        return f"Subject: {self.subject}, Grade: {self.grade}, GWA: {self.GWA}"
    
    def get_student_name(self):
        answer = input("Enter your name: ")
        if answer == "exit":
            return self.exit_confirmation(answer)
        while True:
            if self.string_with_space(answer):
                self.student_name = answer
                print(f"""Hello! {self.student_name} welcome to the GWA calculator.
"yes" or "no" answers are only accepted if you want to exit type "exit".""")
                return self.user_grades()
            else:
                print("Please enter a valid name.")
                return self.get_student_name()

    #validation
    def string_with_space(self, s):
        return bool(re.fullmatch(r"[A-Za-z0-9 ]+", s))
    #validation
    def numbers_only(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    #exit confirmation
    def exit_confirmation(self, answer):
        answer = input("do you want to exit? ")
        if answer in ["yes", "yep", "yeah", "sure", "of course"]:
            self.display_all_subjects_grades()
            exit()
        else:
            return self.response_before_exit(answer)
    
    #response before exit
    def response_before_exit(self, answer):
        answer = input("Do you want to input more grades? ")
        if answer in ["yes", "yep", "yeah", "sure", "of course"]:
            return self.user_grades()
        else:
            return self.show_grades(answer)

    # show grades
    def show_grades(self, answer):
        answer = input("Do you want to see your grades? ")
        if answer in ["yes", "yep", "yeah", "sure", "of course"]:
            if not self.subjects_grades:
                print("No grades available.")
                return self.exit_confirmation(answer)
            self.display_all_subjects_grades()
            return self.exit_confirmation(answer)
        else:
            return self.exit_confirmation(answer)

    def user_grades(self):
        while True:
            try:
                self.subject = input("Enter your subject: ")
                if not self.string_with_space(self.subject):
                    print("Please enter a valid subject.")
                    continue
                elif self.subject == "exit":
                    return self.exit_confirmation(self.subject)

                grade = input("Enter your grade: ")
                if self.numbers_only(grade):
                    self.grade = float(grade)
                else:
                    print("Please enter a valid grade.")
                    continue
                self.subjects_grades.append((self.subject, self.grade))
                return self.follow_up()
            except ValueError:
                print("Please enter a valid grade.")
                continue

    def get_GWA(self):
        grades = [grade for _, grade in self.subjects_grades]
        self.GWA = sum(grades) / len(grades)
        if self.GWA < 2:
            print(f"Your GWA is {self.GWA}. ang galing mo mangopya!")
        else:
            print(f"Your GWA is {self.GWA}. mas talasan pa ang mata!")

    def follow_up(self):
        answer = input("Do you want to input more grades? ").strip().lower()
        if answer in ["yes", "yep", "yeah", "sure", "of course"]:
            return self.user_grades()
        else:
            return self.exit_confirmation(answer)

    def display_all_subjects_grades(self):
        if not self.subjects_grades:
            print("No grades available.")
        else:
            for subject, grade in self.subjects_grades:
                print(f"Subject: {subject}, Grade: {grade}")
            self.get_GWA()
        
if __name__ == "__main__":
    main = main_for_GWA("", "", 0, 0)
    main.get_student_name()
