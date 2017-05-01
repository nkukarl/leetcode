class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initialises an empty list.
        Otherwise initialises a single integer equal to value.
        """
        if value is None:
            self.int_or_list = []
        self.int_or_list = value

    def is_integer(self):
        """
        If this NestedInteger holds a single integer, return True.
        Otherwise, return False.
        """
        if isinstance(self.int_or_list, int):
            return True
        return False

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and
        add a nested integer elem to it.
        """
        if not isinstance(self.int_or_list, list):
            self.int_or_list = []
        self.int_or_list.append(elem)

    def set_integer(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        """
        self.int_or_list = value

    def get_integer(self):
        """
        If this NestedInteger holds a single integer, return the integer.
        Otherwise, return None.
        """
        if isinstance(self.int_or_list, int):
            return self.int_or_list

    def get_list(self):
        """
        If this NestedInteger holds a nested list, return the list.
        Otherwise, return None.
        """
        if isinstance(self.int_or_list, list):
            return self.int_or_list


class Solution(object):
    def deserialize(self, s):
        return self.build(eval(s))

    def build(self, value):
        if isinstance(value, int):
            return NestedInteger(value)
        nested_integer = NestedInteger()
        for v in value:
            if isinstance(v, int):
                nested_integer.add(v)
            else:
                nested_integer.add(self.build(v))
        return nested_integer
