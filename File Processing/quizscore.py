# Accept a quiz score from user
# Convert the score to an int and lookup the corresponding grade
# output the grade

def main():
    score = input("Enter a score between 0 and 5: ")

    grades = ['A', 'B', 'C', 'D', 'E', 'F']

    grades.reverse()
    grade = grades[int(score)]

    print(f'Your grade is {grade}')

main()