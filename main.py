import math
import csv
students = []
students_graded = []

def add_student():
        stud_Id = input("Enter a valid student Id, it will be used to query the database:  ")
        name = input("Enter students Name:  ")
        try:
            age = int(input("Enter Students age:  "))
        except ValueError:
            print('please enter a valid age')
            age = int(input("Enter Students age: "))

        # getting the students subjects and marks
        subjects = {}
        while True:
            subject = input('Enter the Subject Title:  ')
            if subject == 'q':
                break
            try:
                mark = int(input('Enter marks for ' + subject + ': '))
            except:
                print('Please enter a floating point number for the mark')
                mark = float(input('Enter marks for ' + subject + ': '))

            subjects[subject] = mark

        # storing the student details in to the students list
        students.append({'stud_Id': stud_Id, 'name': name, 'age': age, **subjects})

def calculate_grade(students):
    subject_marks = ()
    subject_marks_grade = {}
    students_graded.clear()

    main_count = 0
    # getting an individual student in the list of students
    for student in students:
        subject_marks_grade.clear()
        subject_marks = (x for x in student.items())
        # getting the student details
        subject_count = 0
        grade = ''
        for y in subject_marks:

            if subject_count < 3:
                stud_Id = student['stud_Id']
                stud_name = student['name']
                stud_age = student['age']

            else:
                x = int(y[1])
                if x >= 90:
                    grade = 'A+'
                elif x >= 80:
                    grade = 'A'
                elif x >= 75:
                    grade = 'B+'
                elif x >= 70:
                    grade = 'B'
                elif x >= 60:
                    grade = 'C+'
                elif x >= 50:
                    grade = 'C'
                elif x <= 49 and x > 40:
                    grade = 'E'
                else:
                    grade = 'U'
                subject_grade = y[0] + '_grade'
                subject_marks_grade[y[0]] = y[1]
                subject_marks_grade[subject_grade] = grade



            subject_count += 1

        # deleting the student entries and replacing with the new entry with calculated grades
        students_graded.append({'stud_Id': stud_Id, 'name': stud_name, 'age': stud_age, **subject_marks_grade})

        main_count += 1


    print('Success! go to view students to view their grades')


def update_student(*students):
    stud_id = input('Enter student Id to update student details: ')

    # checking if the student exist in the database
    try:
        count = 0
        for student in students:
            print(student)
            if stud_id == student[count].get('stud_Id'):
                identified_student = student[count]
            count += 1
    except:
        print("student doesn't exist in the database")

    # Editing the student details
    fields = [x for x in identified_student.keys()]
    print('Fields that support Updating: ')

    decision = 'c'
    while True:
        if decision == 'c':
            print(*fields)
            chosenField = input('Enter field to edit and q to quit editing: ')
            update_value = input('Enter update value: ')

            try:
                identified_student[chosenField] = update_value
                print(identified_student)
                decision = input('Enter c to continue eiditing other fields or q to quite editing: ')

            except:
                print('Invalid Field Enter')
        else:
            break


def delete_student(*students):
    stud_id = input('Enter student Id to update student details: ')

    # checking if the student exist in the database
    identified_student = {}
    try:
        count = 0
        for student in students[0]:
            if stud_id == student.get('stud_Id'):
                identified_student = student

                # implementing the deletion of the student
                print(f'Are you sure you want to delete {identified_student["name"]},')
                decision = input('Enter y for yes and n for no:   ')
                if decision == 'y':
                    del students[0][count]
                    print('Deletion was successful')
                else:
                    print('An error occured and Student was not deleted')

            count += 1

    except:
        print("student doesn't exist in the database")



def display_grade(*students):
    identified_student = ''
    stud_id = input('Enter student Id to get students Result: ')

    # checking if the student exist in the database
    try:
        count = 0
        for student in students[0]:
            if stud_id == student.get('stud_Id'):
                identified_student = student
            count += 1

        #printing student details
        print('------------------------------------------------------------------------------------------------------------------------')
        print(f"""
        {identified_student['name']}         Student Id: {identified_student['stud_Id']}          age: {identified_student['age']}
            """)
        print('')

        # calling the statics function
        statistics([student])

        # printing the students results
        print("Student Results")
        print("\t\t Subject \t\t\t\t| \t\t Marks \t\t\t\t | \t\t Grade \t\t\t\t |")
        print("\t\t ------- \t\t \t\t ----- \t\t  \t\t ----- \t\t ")
        marks_grades = (x for x in identified_student.items())
        count = 0
        subject = ''
        mark = ''
        grade = ''

        for x in marks_grades:
            if count >= 3:
                if count % 2 != 0:
                    subject = x[0]
                    mark = x[1]
                    count += 1
                    continue
                else:
                    grade = x[1]

                print(f"\t\t {subject} \t\t\t\t\t| \t\t {mark} \t\t\t\t\t | \t\t {grade} \t\t\t\t |")

            count += 1
    except:
        print("student doesn't exist in the database")


def statistics(students):
    grade_count = {'A+':0,'A':0,'B+':0, 'C+':0, 'C':0, 'U':0}

    main_count = 0
    for student in students:
        grade = (x for x in student.items())
        count = 0
        for y in grade:

            if count >= 3 and count % 2 == 0:
                if y[1] in grade_count:
                    grade_count[y[1]] += 1
                else:
                    grade_count[y[1]] = 1
            count += 1
        main_count += 1
    tuple_grades = list((x for x in grade_count.items() if x[1] > 0))
    sorted_grades = sorted(tuple_grades, key= lambda x: x[1], reverse=True)

    average_index = math.floor(len(sorted_grades) / 2)
    average_grade = sorted_grades[average_index][0]
    # calculating the total number of student past
    total_past = 0
    total_failed = 0
    for key in grade_count:
        if key != 'U' and key != 'E':
            total_past += grade_count[key]
        else:
            total_failed += grade_count[key]
    print('------------------------------------------------------------------------------------------------------------------------')
    print(f"""
     subjects passed: {total_past}\t subjects failed: {total_failed}\t Higest grade: {sorted_grades[0][0]} : {sorted_grades[0][1]}\t Average_Grade: {average_grade} \tLowest grade: {sorted_grades[-1][0]} : {sorted_grades[-1][1]}
            """)
    print('------------------------------------------------------------------------------------------------------------------------')


def save_student_to_file(students):
    print(students)
    fields = [x for x in students[0].keys()]
    print(fields)
    with open('students.csv', 'w', newline='') as students_file:
        students_write = csv.DictWriter(students_file, fieldnames=fields)
        students_write.writeheader()
        students_write.writerows(students)

def read_student_from_file():
    with open('students.csv', 'r') as students_file:
        students_in_file = csv.DictReader(students_file)

        stude = [x for x in students_in_file]
        print('File reading was successful')
        students.clear()
        students.append(stude[0])
        print(students)


# -----------Main-Section-----------------
def display_menu():
    decision = ''
    while decision != 'q':
        print("""
                1. Add Student
                2. Update Student
                3. Delete Student
                4. view Students
                5. Calculate Grad
                6. Statistics
                7. Save Students to file
                8. Read student from file
                ---- q to quit ----
            """)
        decision = input('Enter Choice: ')

        # deciding the function to call based on the users input
        if decision == '1':
            add_student()
        elif decision == '2':
            update_student(students)
        elif decision == '3':
            delete_student(students)
        elif decision == '4':
            display_grade(students_graded)
        elif decision == '5':
            calculate_grade(students)
        elif decision == '6':
            statistics(students_graded)
        elif decision == '7':
            save_student_to_file(students)
        elif decision == '8':
            read_student_from_file()
        else:
            pass


display_menu()






