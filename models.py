import json


class Event:
    id = 1

    def __init__(self, name, address=""):
        self.name = name
        self.address = address
        self.id = Event.id
        Event.id += 1

    def print_info(self):
        print(f"Event ID: {self.id}")
        print(f"Event name: {self.name}")
        print(f"Event address: {self.address}")
        print("----------------")

    def toJSON(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def calculate_limit_people_area(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0


class OnlineEvent(Event):
    def __init__(self, name, _=""):
        local = f"https://tamarcado.com/eventos?id={OnlineEvent.id}"
        super().__init__(name, local)

    def print_info(self):
        print(f"Event ID: {self.id}")
        print(f"Event address: {self.name}")
        print(f"Link to access the event: {self.address}")
        print("----------------")


ev_online = OnlineEvent("Live de Python")
ev2_online = OnlineEvent("Live de JavaScript")
ev = Event("Aula de Python", "Rio de Janeiro")

events = [ev_online, ev2_online, ev]
