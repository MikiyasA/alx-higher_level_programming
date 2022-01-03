#!/usr/bin/python3
"""
The module with class Base and
private class attribute __nb_objects = 0

"""
import json
import os.path
import csv


class Base:
    """ The class Base serve as parent class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Intialization method """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        if id is not None:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ The method returns the JSON string representation
        Args:
             list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ The method write the JASO string represantation on list_objs
        Args:
           list_objs: the list of instance who inherits from class Base
        """

        filename = "{}.json".format(cls.__name__)
        lists = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                lists.append(list_objs[i].to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lists))

    def from_json_string(json_string):
        """ The methods returns the list of the JSON string
        representation json_string:
        Args:
            json_string: string representing a list of dictionaries
        """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ The method that returns an instance with all attributes already set
        Args:
            dictionary: the dictionary with key and value
        """
        if cls.__name__ == "Rectangle":
            n = cls(1, 1)
        else:
            n = cls(1)

        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """ The method that returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            lists = f.read()

        listc = cls.from_json_string(lists)
        listi = []

        for i in range(len(listc)):
            listi.append(cls.create(**listc[i]))

        return (listi)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ The method that save aCSV file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            listd = [0, 0, 0, 0, 0]
            listk = ['id', 'width', 'height', 'x', 'y']
        else:
            listd = ['0', '0', '0', '0']
            listk = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for o in list_objs:
                for k in range(len(listk)):
                    listd[k] = o.to_dictionary()[listk[k]]
                matrix.append(listd[:])

        with open(filename, 'w') as writef:
            writer = csv.writer(writef)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ The method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename)is False:
            return []

        with open(filename, 'r') as readf:
            reader = csv.reader(readf)
            csvlist = list(reader)

        if cls.__name__ == "Rectangle":
            listk = ['id', 'width', 'height', 'x', 'y']
        else:
            listk = ['id', 'size', 'x', 'y']

        matrix = []

        for csvelem in csvlist:
            dictcsv = {}

            for k in enumerate(csvelem):
                dictcsv[listk[k[0]]] = int(k[1])
            matrix.append(dictcsv)

        listi = []

        for i in range(len(matrix)):
            listi.append(cls.create(**matrix[i]))

        return (listi)
