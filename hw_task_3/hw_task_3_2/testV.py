import student, teacher, educational_materials

material_1 = educational_materials.Educational_materials('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')
teacher1 = teacher.Teacher('Ирина', 'Игнатик', 'Александровна', 43, 'f')
st1 = student.Student('Ярослав', 'Гайдуков', 'Эдуардович', 16, 'm')
st2 = student.Student('Максим', 'Трандин', 'Александрович',17, 'm')
st3 = student.Student('Диана', 'Волкова', 'Николаевна', 18, 'f')
st4 = student.Student('Елена', 'Гусева', 'Игоревна', 15, 'f')

teacher1.teach(material_1.Educational_materials[0], st1)
teacher1.teach(material_1.Educational_materials[1], st2, st4)
teacher1.teach(material_1.Educational_materials[2], st2, st3, st4)
teacher1.teach(material_1.Educational_materials[3], st2, st3, st4, st1)
teacher1.teach(material_1.Educational_materials[4], st2, st3, st4, st4)

print('количество обученных учеников учителем 1: ', teacher1.students)
print('Дисциплины студента 1: ', st1.knowledge)
print('Дисциплины студента 2: ', st2.knowledge)
print('Дисциплины студента 3: ', st3.knowledge)
print('Дисциплины студента 4: ', st4.knowledge)


