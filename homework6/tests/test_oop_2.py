import unittest
import pytest

from hw.oop_2 import DeadlineError, Homework, HomeworkResult, Student, Teacher


def test_oop_2():
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    assert result_1.solution ==  "I have done this hw"
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    assert result_2.solution == "I have done this hw too"
    result_3 = lazy_student.do_homework(docs_hw, "done")
    assert result_3.solution == "done"

    with unittest.TestCase.assertRaises(unittest.TestCase, expected_exception=AttributeError):
        HomeworkResult(good_student, "fff", "Solution")

    assert opp_teacher.check_homework(result_1) is True
    temp_1 = opp_teacher.homework_done

    assert advanced_python_teacher.check_homework(result_1) is True
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    assert len(Teacher.homework_done) == 2

    assert str(Teacher.homework_done[oop_hw]) == "{HomeworkResult instance. Solution: I have done this hw}"
    assert Teacher.reset_results() is None
    assert len(Teacher.homework_done) == 0
