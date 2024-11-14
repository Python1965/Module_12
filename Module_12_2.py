# Домашнее задание по теме "Методы Юнит-тестирования"
# ***************************************************************************************
# Задача:
# В первую очередь скачайте исходный код (Можно скопировать), который нужно обложить тестами
# с https://github.com/yanchuki/HumanMoveTest/blob/master/runner_and_tournament.py.
# В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
#
# Изменения в классе Runner:
#   - Появился атрибут speed для определения скорости бегуна.
#   - Метод __eq__ для сравнивания имён бегунов.
#   - Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
#   - Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать
#     и список участников. Также присутствует метод start, который реализует логику бега по предложенной
#     дистанции.
#
# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
#   - setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться
#     результаты всех тестов.
#   - setUp - метод, где создаются 3 объекта:
#       Бегун по имени Усэйн, со скоростью 10.
#       Бегун по имени Андрей, со скоростью 9.
#       Бегун по имени Ник, со скоростью 3.
#   - tearDownClass - метод, где выводятся all_results по очереди в столбец.
#
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
# У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results.
# В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
# (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
#
# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
#   - Усэйн и Ник
#   - Андрей и Ник
#   - Усэйн, Андрей и Ник.
#   - Как можно понять: Ник всегда должен быть последним.
# ****************************************************************************************

import unittest
import runner_2
from pprint import pprint

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_2.Runner('Усейн', 10)
        self.runner2 = runner_2.Runner('Андрей', 9)
        self.runner3 = runner_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    def test_turn1(self):
        self.tur_1 = runner_2.Tournament(90, self.runner1, self.runner3)
        self.all_results = self.tur_1.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    def test_turn2(self):
        self.tur_2 = runner_2.Tournament(90, self.runner2, self.runner3)
        self.all_results = self.tur_2.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_turn3(self):
        self.tur_3 = runner_2.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = self.tur_3.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[3] = self.all_results



if __name__ == '__main__':
    unittest.main()

    def tearDownClass(cls):
        pprint(cls.all_results)