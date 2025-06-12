#get_GWA
#using ternary operator
def get_GWA():
    while gwa > 0:
        gwa = get_grade()
        get_grade()
        print("C" if gwa >= 75 and gwa <= 100 else "FAILED!")

def get_grade(gwa):
    grade = input("user input: ")
        