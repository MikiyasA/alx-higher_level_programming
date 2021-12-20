#!/usr/bin/python3
class MyList(list):
    """ MyList class tha inherits the attribute from class list
    Args:
        list: list class
    """
    def print_sorted(self):
        """ The methon that return sorted list
        Returns:
            sorted values of list
        """
        sorted_list = self.copy()
        print(sorted(sorted_list))
