import csv
# To make formatting easier
import pandas as pd

# main info
filename = "grades.csv"


fields = ['Firstname', 'Lastname', 'Exam1', 'Exam2', 'Exam3']

# creates csv file
def grades(studentNum):
    print(f"Student {studentNum}:")
    name = input("First name: ")
    last = input("Last name: ")
    exam1 = int(input("Exam 1 grade: "))
    exam2 = int(input("Exam 2 grade: "))
    exam3 = int(input("Exam 3 grade: "))

    studentInfo = [name, last, exam1, exam2, exam3]

    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(studentInfo)

# potentially reads file
def readfile():
    print(" ")
    print(" ")
    print(" ")
    cont = input(f'Read file "{filename}"? Answer yes or no: ')
    print(" ")
    if cont.lower() == "yes":
        df = pd.read_csv(filename)
        print(df)

    else:
        print("goodbye.")

# main function
def main():

    studentNum = 0
    cont = input(f"Would you like to write to {filename}? Yes or no: ")
    if cont.lower() == "yes":

        # Number of students to be entered into file
        numStudents = int(input("Number of students: "))
        print(" ")

        # Write header to file
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fields)

            writer.writeheader()

        # Adds students and info to file for each student
        while numStudents != int(studentNum):
            studentNum += 1
            grades(studentNum)


    readfile()

main()