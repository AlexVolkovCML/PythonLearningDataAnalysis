# Класс учебных материалов
# должен принимать любое количество не именованных атрибутов и
# при инициализации сохранять в один атрибут в виде списка.


class Educational_materials:
    def __init__(self, *args):
        self.Educational_materials = [item for item in args]    # любое количество не именованных атрибутов сохраняет в один атрибут в виде списка

    def __len__(self):
        return len(self.Educational_materials)                  # Возвращает количество элементов в контейнере
