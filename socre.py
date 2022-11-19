"""
CP1404 - Practical
Score

"""

SCORE_MIN = 0
SCORE_MID = 50
SCORE_HIGH = 90
SCORE_MAX = 100


def main():
    score = float(input("What is your score? "))
    print(determine_score(score))

def determine_score(score):
    if SCORE_HIGH <= score <= SCORE_MAX:
        print("Excellent")
    elif SCORE_MID <= score < SCORE_HIGH:
        print("Pass")
    elif SCORE_MIN <= score < SCORE_MID:
        print("Bad")
    else:
        print("Invalid input")