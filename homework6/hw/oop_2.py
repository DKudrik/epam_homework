# """
# В этом задании будем улучшать нашу систему классов из задания прошлой лекции
# (Student, Teacher, Homework)
# Советую обратить внимание на defaultdict из модуля collection для
# использования как общую переменную
#
#
# 1. Как то не правильно, что после do_homework мы возвращаем все тот же
# объект - будем возвращать какой-то результат работы (HomeworkResult)
#
# HomeworkResult принимает объект автора задания, принимает исходное задание
# и его решение в виде строки
# Атрибуты:
#     homework - для объекта Homework, если передан не этот класс -  выкинуть
#     подходящие по смыслу исключение с сообщением:
#     'You gave a not Homework object'
#
#     solution - хранит решение ДЗ как строку
#     author - хранит объект Student
#     created - c точной датой и временем создания
#
# 2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
# а не просто принт 'You are late'.
# Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
#
# 3. Student и Teacher имеют одинаковые по смыслу атрибуты
# (last_name, first_name) - избавиться от дублирования с помощью наследования
#
# 4.
# Teacher
# Атрибут:
#     homework_done - структура с интерфейсом как в словаря, сюда поподают все
#     HomeworkResult после успешного прохождения check_homework
#     (нужно гаранитровать остутствие повторяющихся результатов по каждому
#     заданию), группировать по экземплярам Homework.
#     Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
# Методы:
#     check_homework - принимает экземпляр HomeworkResult и возвращает True если
#     ответ студента больше 5 символов, так же при успешной проверке добавить в
#     homework_done.
#     Если меньше 5 символов - никуда не добавлять и вернуть False.
#
#     reset_results - если передать экземпряр Homework - удаляет только
#     результаты этого задания из homework_done, если ничего не передавать,
#     то полностью обнулит homework_done.
#
# PEP8 соблюдать строго.
# Всем перечисленным выше атрибутам и методам классов сохранить названия.
# К названием остальных переменных, классов и тд. подходить ответственно -
# давать логичные подходящие имена.
# """
import datetime as dt
from collections import defaultdict


class DeadlineError(Exception):
    def __init__(self):
        self.text = "You are late"


class HomeworkResult:
    """
    HomeworkResult accepts an author, a homework task and a solution and raises
    AttributeError in case not a Homework object was sent.
    """
    def __init__(self, homework_author, homework, solution: str):
        if isinstance(homework, Homework):
            self.author = homework_author
            self.homework = homework
            self.solution = solution
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
        """
        Checks if the deadline is not over

        :return: bool
        """
        current_date = dt.datetime.now()
        return current_date < self.created + self.deadline


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return f"Student {self.first_name} {self.last_name}"

    def do_homework(self, homework, solution: str) -> HomeworkResult:
        """
        Takes a homework object, a solution and checks if there is still
        enough time for homework. Returns HomeWork result object.

        :param homework: Homework object
        :type homework: Homework class instance
        :param solution: text of a solution
        :type solution: str
        :return: HomeworkResult object
        """

        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError


class Teacher(Student):
    homework_done = defaultdict(set)

    def __str__(self):
        return f"Teacher {self.first_name} {self.last_name}"

    @staticmethod
    def create_homework(text, days):
        """
        Creates a Homework object.

        :param text: String with a homework task
        :param days: Number of days for doing the task
        :return: Homework object
        """
        return Homework(text=text, deadline=days)

    def check_homework(self, homework_result) -> bool:
        """
        Checks if a homework solution meets the requirements

        :param homework_result: HomeworkResult object
        :return: bool
        """
        homework = homework_result.homework
        if len(homework_result.solution) > 5:
            self.homework_done[homework].add(homework_result)
            return True
        return False

    @staticmethod
    def reset_results(homework=None) -> None:
        """
        Removes the result of the defined homework from the storage and
        returns it.
        In case the homework in attributes is not defined - clears
        the whole storage.

        :param homework: Homework object
        :return: None
        """
        if homework:
            Teacher.homework_done.pop(homework)
        else:
            Teacher.homework_done.clear()
