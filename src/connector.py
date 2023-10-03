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
        """Добавляет новую вакансию в JSON-файл"""
        with open(self.filename, 'a', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False)
            file.write('\n')

    def read_json_file(self):
        """Читает и возвращает содержимое JSON-файла в виде списка словарей"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return [json.loads(line) for line in file]
        except FileNotFoundError:
            return []

    def get_vacancies(self, criteria):
        """Возвращает список вакансий, удовлетворяющих заданным критериям"""
        vacancies = self.read_json_file()
        keywords = criteria.get('keywords', [])
        return [vacancy for vacancy in vacancies
                if any(keyword.lower() in vacancy['description'].lower() for keyword in keywords)]

    def delete_vacancies(self, criteria):
        """Удаляет вакансии из файла, удовлетворяющие заданным критериям"""
        vacancies = self.read_json_file()
        keywords = criteria.get('keywords', [])
        vacancies_to_delete = [vacancy for vacancy in vacancies
                               if any(keyword.lower() in vacancy['description'].lower() for keyword in keywords)]

        with open(self.filename, 'w', encoding='utf-8') as file:
            for vacancy in vacancies:
                if vacancy not in vacancies_to_delete:
                    json.dump(vacancy, file, ensure_ascii=False)
                    file.write('\n')
