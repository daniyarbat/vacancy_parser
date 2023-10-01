import json
from abc import ABC, abstractmethod


class AbsConnector(ABC):
    """
    Абстрактный базовый класс, определяет интерфейс для управления файлами с вакансиями
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancies(self, criteria):
        pass


class Connector(AbsConnector):
    """Класс для работы с json-файлами."""

    def __init__(self, filename: str):
        self.filename = filename

    def add_vacancy(self, vacancy):
        """Открывает файл и добавляет новую вакансию в JSON-формате на отдельной строке"""
        with open(self.filename, 'a', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False)
            file.write('\n')

    def get_vacancies(self, string):
        """Считывает содержимое файла, парсит каждую строку вакансии из JSON-формата"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            vacancies = []
            for line in file:
                vacancy = json.loads(line)
                if self.matches_criteria(vacancy, string):
                    vacancies.append(vacancy)
            return vacancies

    def delete_vacancies(self, string):
        """Считывает содержимое файла, удаляет вакансии из файла"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(self.filename, 'w', encoding='utf-8') as file:
            for line in lines:
                vacancy = json.loads(line)
                if not self.matches_criteria(vacancy, string):
                    file.write(line)
