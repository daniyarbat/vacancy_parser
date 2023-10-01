import json


def load_vacancies_from_file(filename: str):
    """Загружает вакансии из JSON-файла и возвращает их в виде списка словарей."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def get_top_n_vacancies(filename: str, n: int):
    """
    Сортирует вакансии по значению зарплаты от наивысшей до наименьшей,
    оставляя только положительные значения зарплаты.
    """
    vacancies = load_vacancies_from_file(filename)
    sorted_vacancies = sorted(vacancies, key=lambda x: x.get('salary_from', 0) or 0, reverse=True)
    filtered_vacancies = [v for v in sorted_vacancies if v.get('salary_from') is not None and v.get('salary_from') > 0]
    return filtered_vacancies[:n]


def get_sorted_vacancies(filename: str):
    """Сортирует вакансии по имени (алфавитный порядок)."""
    vacancies = load_vacancies_from_file(filename)
    return sorted(vacancies, key=lambda x: x['name'])


