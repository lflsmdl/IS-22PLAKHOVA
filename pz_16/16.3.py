# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.
import pickle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

    def diameter(self):
        return 2 * self.radius


def save_del(circles):
    with open('circles.pickle', 'wb') as file:
        pickle.dump(circles, file)

def load_del():
    with open('circles.pickle', 'rb') as file:
        circles = pickle.load(file)
    return circles

circle1 = Circle(5)
circle2 = Circle(7)
circle3 = Circle(10)

circles = [circle1, circle2, circle3]
save_del(circles)

loaded_circles = load_del()

for circle in loaded_circles:
    print("Radius:", circle.radius)
    print("Area:", circle.area())
    print("Circumference:", circle.circumference())
    print("Diameter:", circle.diameter())
    print()