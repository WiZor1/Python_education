class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._Worker__income['wage'] * 12 + self._Worker__income['bonus']


new_pos = Position('Some', 'Body', 'Manager', 13131, 31313)

print(new_pos.get_full_name())
print(new_pos.get_total_income())
