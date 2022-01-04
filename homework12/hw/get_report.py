import datetime as dt
import sqlite3

conn = sqlite3.connect("main.db")
with conn:
    cursor = conn.cursor()
    query = "SELECT * FROM data_homeworkresult"
    cursor.execute(query)
    hw_results = cursor.fetchall()

    data_to_write = []
    for result in hw_results:
        hw_result_created = dt.datetime.strptime(result[2], "%Y-%m-%d %H:%M:%S")
        homework_id = result[4]
        query = f"SELECT * FROM data_homework WHERE id = {homework_id}"
        cursor.execute(query)
        hw_data = cursor.fetchone()
        teacher_id = hw_data[4]
        hw_deadline = hw_data[2]
        hw_created = dt.datetime.strptime(hw_data[3], "%Y-%m-%d %H:%M:%S.%f")

        if hw_result_created < (hw_created + dt.timedelta(hw_deadline)):
            student_id = result[3]
            query = f"SELECT * FROM data_student WHERE id = {student_id}"
            cursor.execute(query)
            student_data = cursor.fetchone()
            student_name = student_data[1] + " " + student_data[2]

            query = f"SELECT * FROM data_teacher WHERE id = {teacher_id}"
            cursor.execute(query)
            teacher_data = cursor.fetchone()
            teacher_name = teacher_data[1] + " " + teacher_data[2]
            data_to_write.append(
                [student_name, str(hw_created).split(".")[0], teacher_name]
            )

    with open("db_data.csv", "x", newline="") as file:
        file.write("%s;" % "Student's name")
        file.write("%s;" % "Creation date")
        file.write("%s;" % "Teacher's name")
        file.write("\n")

        for row in data_to_write:
            for column in row:
                file.write("%s;" % column)
            file.write("\n")
conn.close()
