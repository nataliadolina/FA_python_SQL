from datetime import timedelta

from OOP.task_19.PersonTypes import Entrant, Student, Teacher

base = [Entrant("Павлов", 14, 9, 2004, "it"), Entrant("Авернина", 5, 7, 1998, "marketing"),
        Entrant("Чигунихина", 17, 1, 2003, "art"), Entrant("Протасова", 14, 9, 2000, "design"),
        Entrant("Мун", 14, 9, 1987, "philosophy"), Student("Cиницин", 8, 7, 1999, "it", 3),
        Student("Рогожкин", 8, 7, 1957, "art", 1), Student("Мирная", 1, 1, 2004, "design", 1),
        Student("Тютьнева", 31, 12, 1997, "art", 3),
        Teacher("Касаткина", 12, 12, 1978, "art", "учитель китайского", timedelta(days=8046)),
        Teacher("Чермных", 12, 12, 1995, "it", "учитель программирования на java", timedelta(days=1934))]


def select_by_age(min_age, max_age, sp):
    return list(filter(lambda x: min_age <= x.age < max_age, sp))


def print_persons(sp):
    for i in sp:
        print(i)
        print()


print_persons(select_by_age(17, 25, base))
