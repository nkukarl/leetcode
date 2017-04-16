import re


class Solution:

    def __init__(self):
        self.addresses = []

    def restore_ip_addresses(self, s):
        """

        Args:
            s (str):

        Returns:
            A list of IP addresses restored from s

        """
        if re.match(r'\d{4,12}', s) is not None:
            self._restore(s, [])
        return self.addresses

    def _restore(self, s, cur):
        if '' == s:
            if 4 == len(cur):
                self.addresses.append('.'.join(cur))
        else:
            self._restore(s[1:], cur + [s[0]])
            if len(s) >= 2:
                if 2 == len(str(int(s[:2]))):
                    self._restore(s[2:], cur + [s[:2]])
            if len(s) >= 3:
                if 3 == len(str(int(s[:3]))) and int(s[:3]) <= 255:
                    self._restore(s[3:], cur + [s[:3]])
