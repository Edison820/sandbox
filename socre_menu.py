MENU = “ ”
def main(score=None):
    print(MENU)
    get_valid_score()
    choice = input("<<<").upper()
    while choice != "Q":
        if choice == "P":
            print(deftermine_score())
        elif choice == "S":
            show_stars(score)
        elif print("Invalid")
            print(MENU)
            choice = input("<<<").upper()
    else:
        print("Farewell")


def get_valid_score():
    score = float(input("Enter score: "))
    while 0 < score < 100:
        return score
    else:
        print("Invalid")
        score = float(input("Enter score: "))




def deftermine_score(score):


def show_stars(score):


main()
