class Solution(object):
    def compare_version(self, v1, v2):
        v1 = list(map(int, v1.split('.')))[::-1]
        v2 = list(map(int, v2.split('.')))[::-1]
        # Compare each segment of version number
        while len(v1) > 0 and len(v2) > 0:
            vv1, vv2 = v1.pop(), v2.pop()
            if vv1 < vv2:
                return -1
            if vv1 > vv2:
                return 1
            continue

        # Need to handle scenarios like v1 = "1.0.0" and v2 = "1"
        # In this case, v1 is equal to v2
        if v1 == [] == v2 \
                or ([] == v1 and 0 == sum(v2)) \
                or ([] == v2 and 0 == sum(v1)):
            return 0
        # If there are segments remaining from v2, then v2 is older than v1.
        # Otherwise, v1 is older than v2.
        if [] == v1:
            return -1  # v2 is older than v1
        return 1  # v1 is older than v2
