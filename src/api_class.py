import os
import requests
from abc import ABC, abstractmethod
from vacancy import Vacancy

class AbstractApiClass(ABC):
    """
    Абстрактный класс для работы с API.
    """
    @abstractmethod
    def get_vacancies(self, *args):
        pass

class BaseAPI(AbstractApiClass):
    """
    Базовый класс с общими параметрами для двух api классов
    """
    def __init__(self, api_url, params):
        self.api_url = api_url
        self.params = params

    def get_vacancies(self):
        """
        Метод для получения вакансий с сайта
        """
        try:
            response = requests.get(self.api_url, params=self.params)
            response.raise_for_status()  # Проверка на ошибки HTTP
            data = response.json()
            return self._parse_vacancies(data)
        except requests.exceptions.RequestException as e:
            raise Exception(f'Ошибка при запросе данных о вакансиях: {e}')

    @abstractmethod
    def _parse_vacancies(self, data):
        pass

class HeadHunterAPI(BaseAPI):
    """
    Класс для работы с api hh.ru
    """
    def __init__(self, area=1, text='python', per_page=10):
        api_url = 'https://api.hh.ru/vacancies'
        params = {'area': area, 'text': text, 'per_page': per_page}
        super().__init__(api_url, params)

    def _parse_vacancies(self, data):
        """
        Метод для парсинга вакансий с сайта
        """
        hh_vacancies = []
        for item in data.get('items', []):
            salary = item.get('salary', {})
            try:
                vacancy = Vacancy(
                    name=item['name'],
                    url=item['url'],
                    description=item['snippet']['requirement'],
                    salary_to=salary.get('to'),
                    salary_from=salary.get('from')
                )
                hh_vacancies.append(vacancy)
            except KeyError:
                continue
        return hh_vacancies
