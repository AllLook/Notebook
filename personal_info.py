class PersonalInfo:

    def add_personal_data(self):
        self.name = input("Введите имя: ")
        self.data = input("Введите данные: ")
        return self.name, self.data

    def __init__(self, name: str, data: str):
        self.name = name
        self.data = data

    def __str__(self):
        return f"{self.name} - {self.data}"

    def __repr__(self):
        return f"PersonalInfo({self.name}, {self.data})"
