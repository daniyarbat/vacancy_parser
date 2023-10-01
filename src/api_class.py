from abc import ABC, abstractmethod
import requests
#from vacancy import Vacancy

class AbstractApiClass(ABC):
    @abstractmethod
    def get_vacancies(self, *args):
        pass

class BaseAPI(AbstractApiClass):
    def __init__(self, api_url, params):
        self.api_url = api_url
        self.params = params
