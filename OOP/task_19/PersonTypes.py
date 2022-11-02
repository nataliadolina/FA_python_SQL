from datetime import timedelta

from OOP.task_19.Person import Person


class Entrant(Person):
    def __init__(self, surname, day_birth, month_birth, year_birth, faculty):
        super().__init__(surname, day_birth, month_birth, year_birth, faculty)
        self.name = "абитуриенте"


class Student(Person):
    def __init__(self, surname, day_birth, month_birth, year_birth, faculty, course):
        super().__init__(surname, day_birth, month_birth, year_birth, faculty)
        self.name = "студенте"
        self.course = course

    def __str__(self):
        return self.get_main_info() + f"\n Курс - {self.course}"


class Teacher(Person):
    def __init__(self, surname, day_birth, month_birth, year_birth, faculty, post, exp: timedelta):
        super().__init__(surname, day_birth, month_birth, year_birth, faculty)
        self.name = "преподавателе"
        self.exp = exp
        self.post = post

    def __str__(self):
        return self.get_main_info() + f"\n Должность - {self.post}" \
                                      f"\n Стаж - {self.exp.days // 365}"
