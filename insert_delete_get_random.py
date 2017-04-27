import random


class RandomizedSet(object):
    def __init__(self):
        self.vals = set()

    def insert(self, val):
        """

        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.

        """
        if val not in self.vals:
            self.vals.add(val)
            return True
        return False

    def remove(self, val):
        """

        Removes a value from the set.
        Returns true if the set contained the specified element.

        """
        if val in self.vals:
            self.vals.remove(val)
            return True
        return False

    def getRandom(self):
        """

        Get a random element from the set.

        """
        return random.sample(self.vals, 1)[0]
