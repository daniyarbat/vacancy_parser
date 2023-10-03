from .vacancy import Vacancy
import json


def load_vacancies_from_file(filename: str):
    """Загружает вакансии из JSON-файла и возвращает их в виде списка словарей."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def get_vacs(vacancies):
    """
    Принимает список словарей с данными о вакансиях и возвращает список экземпляров класса Vacancy.
    """
    all_vacancies = []
    for vacancy in vacancies:
        all_vacancies.append(Vacancy(name=vacancy["name"],
                                     url=vacancy["url"],
                                     salary_from=vacancy["salary_from"],
                                     salary_to=vacancy["salary_to"],
                                     description=vacancy["description"]))
    return all_vacancies


def get_top_n_vacancies(filename: str, n: int):
    """
    Сортирует вакансии по значению зарплаты от наивысшей до наименьшей,
    оставляя только положительные значения зарплаты.
    """
    vacancies = load_vacancies_from_file(filename)
    sorted_vacancies = sorted(vacancies, key=lambda x: x.get('salary_from', 0) or 0, reverse=True)
    filtered_vacancies = [v for v in sorted_vacancies if v.get('salary_from') is not None and v.get('salary_from') > 0]
    return get_vacs(filtered_vacancies[:n])


def get_sorted_vacancies(filename: str):
    """Сортирует вакансии по имени (алфавитный порядок)."""
    vacancies = load_vacancies_from_file(filename)
    sorted_vacancies = sorted(vacancies, key=lambda x: x.get('name', ''))
    return get_vacs(sorted_vacancies)


def get_vacancies_with_description(filename: str, keywords):
    """Фильтрует вакансии, оставляя только те, у которых описание содержит заданные ключевые слова."""
    vacancies = load_vacancies_from_file(filename)
    filtered_vacancies = [vacancy for vacancy in vacancies
                          if any(keyword.lower() in vacancy.get('description', '').lower() for keyword in keywords)]
    return get_vacs(filtered_vacancies)
