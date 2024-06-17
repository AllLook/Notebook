class Event:

    def add_event(self):
        self.data_event = input("Введите дату события: ")
        self.task = input("Введите описание задачи:")
        return self.data_event, self.task

    def __init__(self, data_event: str, task: str):
        self.data_event = data_event
        self.task = task

    def __str__(self):
        return f"На дату {self.data_event} назначено событие {self.task}"

    def __repr__(self):
        return f"Event({self.data_event}, {self.task})"

