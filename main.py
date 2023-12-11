"""Збереження та завантаження об'єкту класу:
Створіть клас з полями та методами.
Створіть об'єкт цього класу.
Використайте pickle для збереження цього об'єкту у файлі.
Використайте gzip для стиснення цього файлу.
Потім завантажте стиснений файл, розпакуйте його з gzip
та використайте pickle для завантаження об'єкту."""

import pickle
import gzip

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name {self.name}, age: {self.age}")

obj = MyClass("Vasia", 30)
with open("object_file.pickle", 'wb') as file:
    pickle.dump(obj, file)


with open("object_file.pickle", "rb") as file:
    data = file.read()
    with gzip.open("compressed_object_file.pickle.gz", "wb") as compressed_file:
        compressed_file.write(data)
    print("Файл стиснуто!")

with gzip.open("compressed_object_file.pickle.gz", "rb") as compressed_file:
    uncompressed_file = compressed_file.read()
    with open("uncompressed_object_file.pickle", 'wb') as file:
        file.write(uncompressed_file)
    print("Файл розпаковано!")

with open("uncompressed_object_file.pickle", "rb") as file:
    loaded_obj = pickle.load(file)

loaded_obj.display_info()