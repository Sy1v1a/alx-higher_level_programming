#!/usr/bin/python3
"""Defines class Base"""
import json
import csv
import turtle


class Base:
    """Reps class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Args:
            id: empty para..."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert to json str"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save file to json"""
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string\
            ([obj.to_dictionary() for obj in list_objs]) \
            if list_objs is not None else "[]"
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Import fron json"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create cls file"""
        if cls.__name__ == "Rectangle":
            ex_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            ex_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        ex_instance.update(**dictionary)
        return ex_instance

    @classmethod
    def load_from_file(cls):
        """Load from cls to json"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_data = file.read()
        except FileNotFoundError:
            return []

        datalist = cls.from_json_string(json_data)
        exinstance = [cls.create(**data) for data in datalist]
        return exinstance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to csv"""
        filename = cls.__name__ + ".csv"
        fieldnames = cls.get_fieldnames()

        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load fron cls to csv"""
        filename = cls.__name__ + ".csv"
        exinstance = []

        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                exinstance.append(cls.create(**row))

        return exinstance

    @staticmethod
    def get_fieldnames():
        """Get file names"""
        return ["id", "width", "height", "x", "y"]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw with the aid of turtle"""
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Draw Rectangles and Squares")
        turtle.speed(2)

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.color("blue")
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("red")
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.done()
