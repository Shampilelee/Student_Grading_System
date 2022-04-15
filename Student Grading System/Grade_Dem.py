
class Grade_User:

    totMarks = 0.0


    # This Method Calculates And Display's The Student's Grade

    def student_grade(clas_wrk, clas_tst, mid_sem, exams):
        totMarks = clas_wrk + clas_tst + mid_sem + exams

        if totMarks >= 90.0:
            print("With " + str(totMarks) + " marks, you had: A ")
        elif totMarks >= 80.0:
            print("With " + str(totMarks) + " marks, you had: B ")
        elif totMarks >= 70.0:
            print("With " + str(totMarks) + " marks, you had: C ")
        elif totMarks >= 50.0:
            print("With " + str(totMarks) + " marks, you had: D ")
        else:
            print("With " + str(totMarks) + " marks, you failed ")
    


    # This Method Displays The Student's Details

    def show_student_details(full_nam, cours, index_num, gender):

        print("Name: " + full_nam.upper())
        print("Course: " + cours.upper())
        print("Index Number: " + index_num)
        print("Gender: " + gender.upper())
        