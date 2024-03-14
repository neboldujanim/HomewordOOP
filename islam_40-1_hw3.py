class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu):
        self.__cpu = cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory):
        self.__memory = memory\

    def make_computations(self):
        plus = self.__cpu + self.__memory
        minus = self.__cpu - self.__memory
        multiply = self.__cpu * self.__memory
        if self.__memory == 0:
            print('на ноль делить НЕЛЬЗЯ')
            devide = None
        else:
            devide = self.__cpu / self.__memory

        return f'plus-{plus}\nminus-{minus}\ndevide-{round(devide, 1)}\nmultiply-{multiply}\n'

    def __str__(self):
        return f"Computer(cpu={self.cpu}, memory={self.memory})"

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, sim_cards):
        self.__sim_cards_list = sim_cards

    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до локации {location}")

    def __str__(self):
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})"



computer = Computer(16, 512 )
phone = Phone(["Beeline", "Megacom", "O!"])
smartphone1 = SmartPhone(6, 12, 'Megacom')
smartphone2 = SmartPhone(16, 56, "Beeline" )


print(computer)
print(phone)
print(smartphone1)
print(smartphone2)


computer.make_computations()
phone.call(1, "+996 555 123456")
smartphone1.use_gps("дом")
smartphone2.use_gps("работа")

print('< ', computer < Computer(12, 64))
print('> ',computer  <= Computer(10, 512))
print('<= ',computer == Computer(14, 1024))
print('== ', computer >=  Computer(8, 1024))
print('>= ', computer !=  Computer(16, 512))
print('!= ', computer > Computer(12, 64))
