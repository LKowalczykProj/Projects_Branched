from enum import Enum


class Gender(Enum):
    Male = "male"
    Female = "female"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    def __str__(self):
        return self.value


class HairColor(Enum):
    Blond = "blond"
    Black = "black"
    Brown = "brown"
    Red = "red"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    def __str__(self):
        return self.value


class Ethnicity(Enum):
    White = "white"
    Black = "black"
    Yellow = "yellow"
    Brown = "brown"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    def __str__(self):
        return self.value


class Country(Enum):
    USA = "USA"
    Australia = "Australia"
    China = "China"
    Canada = "Canada"
    Europe = "Europe"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    def __str__(self):
        return self.value
