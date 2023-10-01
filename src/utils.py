import json


def load_vacancies_from_file(filename: str):
    """Загружает вакансии из JSON-файла и возвращает их в виде списка словарей."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []



