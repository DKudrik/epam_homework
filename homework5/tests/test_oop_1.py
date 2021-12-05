import datetime as dt

import pytest

from hw.oop_1 import Homework, Student, Teacher


@pytest.fixture()
def test_data():
    actual_hw = Homework("Hello", 5)
    expired_hw = Homework("world", 0)
    student = Student("Petrov", "Ivan")
    teacher = Teacher("De Niro", "Robert")
    return actual_hw, expired_hw, student, teacher


def test_homework_class(test_data):
    actual_hw, expired_hw, _, _ = test_data
    assert actual_hw.text == "Hello"
    assert actual_hw.is_active() == True
    assert expired_hw.text == "world"
    assert expired_hw.is_active() == False


def test_student_class(test_data):
    actual_hw, expired_hw, student, _ = test_data
    assert student.first_name == "Ivan"
    assert student.last_name == "Petrov"
    assert student.do_homework(actual_hw) == actual_hw
    assert student.do_homework(expired_hw) is None


def test_teacher_class(test_data):
    _, _, _, teacher = test_data
    hw1 = teacher.create_homework("Test", 4)
    assert teacher.first_name == "Robert"
    assert teacher.last_name == "De Niro"
    assert isinstance(hw1, Homework)
    assert hw1.deadline == dt.timedelta(days=4)
