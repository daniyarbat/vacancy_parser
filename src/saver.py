import json


class JsonSaver:
    """Класс для сохранения информации о вакансиях в JSON-файл."""

    def __init__(self, filename: str):
        self.filename = filename

    def load_existing_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def write_vacancies(self, vacancies):
        existing_data = self.load_existing_data()

        new_data = []
        for vacancy in vacancies:
            new_data.append({
                'name': vacancy.name,
                'url': vacancy.url,
                'description': vacancy.description,
                'salary_to': vacancy.salary_to,
                'salary_from': vacancy.salary_from
            })

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, ensure_ascii=False, indent=4)
