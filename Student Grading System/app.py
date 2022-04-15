from Grade_Dem import Grade_User

error = False

# The Program Collects Data From The Student

print('\n\n  $  | Personal Data |  $ \n')

student_name = input("Kindly enter your fullname: ")
student_course = input(str('\n') + "Enter your course of student: ")
student_index_number = input(str('\n') + "Enter your index number: ")
student_gender = input(str('\n') + "Enter your gender: ")


try:
    print('\n\n    $  | Marks Data |  $ \n')
    
    class_work_Mrks = float(input("Enter your class work marks: "))
    if class_work_Mrks > 10:
        print(str('\n') + " || Class_Work Marks Should Not Be More Than '10', Kindly Reboot The Program. || " + str('\n'))
        exit()
    
    class_test_Mrks = float(input(str('\n') + "Enter your class test marks: "))
    if class_test_Mrks > 10:
        print(str('\n') + " || Class_Test Marks Should Not Be More Than '10', Kindly Reboot The Program. || " + str('\n'))    
        exit()

    mid_sem_Mrks = float(input(str('\n') + "Enter your mid-sem marks: "))
    if mid_sem_Mrks > 20:
        print(str('\n') + " || Mid_Sem Marks Should Not Be More Than '20', Kindly Reboot The Program. || " + str('\n'))
        exit()
    
    exams_Mrks = float(input(str('\n') + "Enter your exams marks: "))
    if exams_Mrks > 60:
        print(str('\n') + " || Exams Marks Should Not Be More Than '60', Kindly Reboot The Program. || " + str('\n'))
        exit()

except ValueError:
    print(str('\n') + " || Please Numbers Only, Kindly reboot the program and enter numbers. || " + str('\n'))
    exit()

    

print("\n processing... \n")


Grade_User.show_student_details(student_name, student_course, student_index_number, student_gender)
Grade_User.student_grade(class_work_Mrks, class_test_Mrks, mid_sem_Mrks, exams_Mrks)
print()
print("Congratulations :D :D ")
