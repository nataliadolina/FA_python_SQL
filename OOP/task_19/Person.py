from datetime import date, timedelta


class TimeDelta(timedelta):
    def __str__(self):
        return f"{self.days} лет"


class Person:
    def __init__(self, surname, day_birth, month_birth, year_birth, faculty):
        self.surname = surname
        self.date_birth = date(year=year_birth, month=month_birth, day=day_birth)
        self.name = "Человек"
        self.faculty = faculty
        self.age = self.age()

    def age(self):
        age = abs(date.today() - self.date_birth)
        return age.days // 365

    def get_main_info(self):
        string = f"Информация о {self.name}:\n Фамилия - {self.surname.capitalize()}" \
               f" \n Дата рождения - {self.date_birth.strftime('%A %d. %B %Y')}" \
               f"\n Факультет - {self.faculty}" \
               f"\n Возраст - {self.age} лет."
        return string

    def __str__(self):
        return self.get_main_info()
