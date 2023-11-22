from hw_task_3.hw_task_3_2.person import Person      # импорт класса
import random                                        # библиотека для генерации сл. чисел

#У каждого ученика должен быть атрибут “knowledge” - список знаний.
#		Для ученика создайте метод “take”
#-	метод принимает строку знаний и добавляет ее в список знаний ученика.


class Student(Person):
    def __init__(self, first_name, last_name, surname, age, gender):
        super().__init__(first_name, last_name, surname, age, gender)            #для получения доступа из класса наследника к методам класса-родителя в том случае, если наследник переопределил эти методы
        self.knowledge = []                                                      # добавлен атрибут “knowledge” - список знаний

    def take(self, topic):                                                       #метод принимает строку знаний и добавляет ее в список знаний ученика
        self.knowledge.append(topic)

    def __len__(self):                                                           # Возвращает количество элементов в списке
        return len(self.knowledge)

    def forget(self):                                                            #метод, позволяющий ученику случайно "забывать" какую-нибудь часть своих знаний
        self.knowledge.pop(random.choice(range(len(self.knowledge))))