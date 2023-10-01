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

