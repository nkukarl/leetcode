# class NestedInteger(object):
#     def is_integer(self):
#         """
#         Return True if this NestedInteger holds a single integer
#         rather than a nested list.
#         """
#
#     def get_integer(self):
#         """
#         Return the single integer that this NestedInteger holds
#         if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         """
#
#     def get_list(self):
#         """
#         Return the nested list that this NestedInteger holds
#         if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         """


class NestedIterator(object):
    def __init__(self, nested_list):
        self.flattened_list = []
        self.flatten(nested_list)
        self.flattened_list.reverse()

    def flatten(self, nested_list):
        for n_i in nested_list:
            if n_i.is_integer():
                self.flattened_list.append(n_i.get_integer())
            else:
                self.flatten(n_i.get_list())

    def next(self):
        return self.flattened_list.pop()

    def has_next(self):
        return len(self.flattened_list) > 0


class NestedIteratorSelf(object):
    def __init__(self, nested_list):
        self.flattened_list = []
        self.flatten(nested_list)
        self.flattened_list.reverse()

    def flatten(self, nested_list):
        for int_or_nl in nested_list:
            if isinstance(int_or_nl, int):
                self.flattened_list.append(int_or_nl)
            else:
                self.flatten(int_or_nl)

    def next(self):
        return self.flattened_list.pop()

    def has_next(self):
        return len(self.flattened_list) > 0
