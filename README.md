# Student-Management-system
## This is a python console application.
It has the ability to add student, delete student, update student, caculate student grades, save students data to file, read student from file, display the student grades, give students statistics. It also has a user driven menu. 
This student management system has the following functions
1. add_student()
    It takes in the students name, age, ID number and it has a dynamic way of adding student subjects and marks. This student information is stored in a dictionary which is later stored to the students list which is a global variable.
2. update_student()
   This function takes in the students ID number and checks if the student exist in the students list and then displays the students fields that support Editing. when a field is entered for editing, it prompts for a value for that field then update that student in the students list with the inputed data.
3. delete_student()
   It takes in the students ID number and check if that student is in the student list, and if yes, it prompst the user with the students data and ask the user to enter y to proceed with the deletion and c to cancel deletion. if y, then it deletes that student from the students list.
4. calculate_grade()
   this function gets each student in the students list and then loop through all of that students subjects and marks then grades the student and store the graded student in the students_graded list which is also a global variable.
5. display_grade()
   this function prompts for the students ID number and then display the student name, age, Id number and the subjects with its corresponding marks and grades. It also display the highest, average and lowest subject a student scored in based on the grade the studen has for that subject
6. save_student_to_file() and read_student_from_file()
   These functions saves and reads the student from file and it does it in a csv format. it saves the ungraded student to file.
7. display_menu()
   this function displays all the options a user has, then receives the users input and then invoke a function assign to the coresponding value.
