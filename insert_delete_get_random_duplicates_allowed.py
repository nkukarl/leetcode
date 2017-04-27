import random


class RandomizedCollection(object):
    def __init__(self):
        # Use self.vals to store all the elements
        self.vals = []
        # Use element:set([indices]) as key:value pairs to store position info
        self.pos = {}

    def insert(self, val):
        """

        Inserts a value to the collection.
        If the collection did not already contain the specified element:
            return True.
        Else:
            Return False.

        """
        if val not in self.pos:
            flag = True
        else:
            flag = False
        self.vals.append(val)
        if self.pos.get(val) is None:
            self.pos[val] = set()
        self.pos[val].add(len(self.vals) - 1)
        return flag

    def remove(self, val):
        """

        Removes a value from the collection.
        If the collection contained the specified element:
            returns True.
        Else:
            return False.

        """
        if self.pos.get(val) not in [set(), None]:
            # Find the indices of val
            indices = self.pos[val]
            index = self.pop_from_set(indices)
            # Only need to swap elements if index is not the last
            if index != len(self.vals) - 1:
                # Update position info before swapping elements
                self.pos[self.vals[-1]].remove(len(self.vals) - 1)
                self.pos[self.vals[-1]].add(index)
                # Swap val with the last element of self.vals
                self.vals[index], self.vals[-1] = self.vals[-1], self.vals[
                    index]
            # Remove the last element of self.vals
            self.vals.pop()
            return True
        return False

    def pop_from_set(self, s):
        """

        Randomly pop an element from a set.

        Args:
            s (set):

        """
        e = None
        for e in s:
            break
        if e is not None:
            s.remove(e)
        return e

    def get_random(self):
        """

        Get a random element from the collection.

        """
        return random.choice(self.vals)
