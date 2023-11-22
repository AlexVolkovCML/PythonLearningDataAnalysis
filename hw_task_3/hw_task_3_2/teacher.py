from hw_task_3.hw_task_3_2.person import Person      # импорт класса


class Teacher(Person):
    def __init__(self, first_name, last_name, surname, age,  gender):
        super().__init__(first_name, last_name, surname, age, gender)     #для получения доступа из класса наследника к методам класса-родителя в том случае, если наследник переопределил эти методы
        self.students = 0                                                 # количество обученных учеников

    def teach(self, edu_materials, *stud):
        students = [item for item in stud]                                # определяется список учеников из edu_materials
        for s in students:
            s.take(edu_materials)
            self.students = self.students + 1                             # счетчик количества обученных учеников

