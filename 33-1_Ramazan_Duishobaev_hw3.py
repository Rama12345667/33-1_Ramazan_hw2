class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f"Computer (CPU: {self.__cpu}, Memory: {self.__memory})"

    def __eq__(self, other):
        return self.__memory == other.get_memory()

    def __lt__(self, other):
        return self.__memory < other.get_memory()

    def __le__(self, other):
        return self.__memory <= other.get_memory()

    def __gt__(self, other):
        return self.__memory > other.get_memory()

    def __ge__(self, other):
        return self.__memory >= other.get_memory()

    def __ne__(self, other):
        return self.__memory != other.get_memory()


class Phone:
    def __init__(self):
        self.__sim_cards_list = []

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if 0 <= sim_card_number < len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number + 1} - {sim_card}")
        else:
            print("Недопустимый номер сим-карты")

    def __str__(self):
        return f"Phone (Sim Cards: {self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self)

    def use_gps(self, location):
        print(f"Проложение маршрута до локации: {location}")

    def __str__(self):
        return f"SmartPhone (CPU: {self.get_cpu()}, Memory: {self.get_memory()}, Sim Cards: {self.get_sim_cards_list()})"


computer = Computer(cpu=2.4, memory=8)
phone = Phone()
phone.set_sim_cards_list(["Beeline", "MegaCom", "O"])
smartphone1 = SmartPhone(cpu=2.8, memory=16)
smartphone2 = SmartPhone(cpu=3.0, memory=32)

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

computer_result = computer.make_computations()
print(f"Computer computations result: {computer_result}")

phone.call(sim_card_number=0, call_to_number="+996 777 99 88 11")

smartphone1.use_gps(location="123.456,789.012")

print("Comparison between computers:")
print(f"Computer 1 memory > Computer 2 memory: {computer > smartphone1}")
print(f"Computer 2 memory <= Computer 1 memory: {smartphone2 <= computer}")
print(f"Computer 1 memory == Computer 2 memory: {computer == smartphone2}")