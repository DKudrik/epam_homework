"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime as dt
from collections import defaultdict


class DeadlineError(Exception):
    def __init__(self):
        self.text = "You are late"


class HomeworkResult:
    def __init__(self, homework_obj_author, homework_obj, solution: str):
        if isinstance(homework_obj, Homework):
            self.homework = homework_obj
            self.solution = solution
            self.author = homework_obj_author
            self.created = dt.datetime.now()
        else:
            raise AttributeError("You gave a not Homework object")

    def __repr__(self):
        return f"HomeworkResult instance. Solution: {self.solution}"


class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = dt.timedelta(days=deadline)
        self.created = dt.datetime.now()

    def __str__(self):
        return (
            f"Homework object. Text: {self.text}, deadline:{self.deadline},"
            f"created:{self.created}"
        )

    def __repr__(self):
        return f"Homework instance. Text: {self.text}"

    def is_active(self) -> bool:
        """Homework object method - checks if the deadline is not over"""
        current_date = dt.datetime.now()
        return current_date < self.created + self.deadline


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return f"Student {self.first_name} {self.last_name}"

    def do_homework(self, homework_object, solution: str) -> HomeworkResult:
        """
        Takes a homework object, a solution and checks if there is still
        enough time for homework. Returns HomeWork result object.
        """
        result = HomeworkResult(self, homework_object, solution)
        if homework_object.is_active():
            return result
        raise DeadlineError


class Teacher(Student):
    homework_done = defaultdict(set)

    def __str__(self):
        return f"Teacher {self.first_name} {self.last_name}"

    @staticmethod
    def create_homework(text, days):
        """Creates a Homework object."""
        return Homework(text=text, deadline=days)

    def check_homework(self, homework_result_obj):
        homework = homework_result_obj.homework
        if len(homework_result_obj.solution) > 5:
            self.__class__.homework_done[homework].add(homework_result_obj)
            return True
        return False

    @staticmethod
    def reset_results(homework_obj=None):
        if homework_obj:
            Teacher.homework_done.pop(homework_obj)
        else:
            Teacher.homework_done.clear()


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()