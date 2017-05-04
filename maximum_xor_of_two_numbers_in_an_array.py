# TODO: Understand this!
class Solution(object):
    def find_maximum_xor(self, nums):
        r = 0
        l = [[nums, nums]]
        for i in range(4, -1, -1):
            count = 0
            newL = []
            for pair in l:
                zz, zo = [], []
                for zero in pair[0]:
                    if (zero >> i) & 1 == 0:
                        zz.append(zero)
                    else:
                        zo.append(zero)
                oz, oo = [], []
                for one in pair[1]:
                    if (one >> i) & 1 == 0:
                        oz.append(one)
                    else:
                        oo.append(one)
                if len(zz) > 0 and len(oo) > 0:
                    newL.append([zz, oo])
                    count += 1
                if len(zo) > 0 and len(oz) > 0:
                    newL.append([zo, oz])
                    count += 1
            if count > 0:
                l = newL
                r += 1 << i
        return r
