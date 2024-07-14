class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name) -> bool:
        if not self.openseats():
            return False
        self.passengers.append(name)
        return True

    def openseats(self) -> int:
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print("Succesfully added " + person + " to the flight")
    else:
        print("No avaliable seats for " + person)