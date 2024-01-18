#!/usr/bin/python3

""" Define class Base """

class Base:
    __nb_objects = 0

    """ assign the public instance attribute id """

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
