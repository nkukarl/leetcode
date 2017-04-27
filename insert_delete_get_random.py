import random


class RandomizedSet(object):
    def __init__(self):
        # Use self.vals to store all the elements
        self.vals = []
        # Use element:index as key:value pairs to store position info
        self.pos = {}

    def insert(self, val):
        """

        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.

        """
        if val not in self.pos:
            self.vals.append(val)
            self.pos[val] = len(self.vals) - 1
            return True
        return False

    def remove(self, val):
        """

        Removes a value from the set.
        Returns true if the set contained the specified element.

        """
        if val in self.pos:
            # Find the index of val
            index = self.pos[val]
            # Update position info before swapping elements
            self.pos[self.vals[-1]] = index
            # Swap val with the last element of self.vals
            self.vals[index], self.vals[-1] = self.vals[-1], self.vals[index]
            # Remove the last element of self.vals
            self.vals.pop()
            # Remove position info from self.pos
            del self.pos[val]
            return True
        return False

    def get_random(self):
        """

        Get a random element from the set.

        """
        return random.choice(self.vals)
