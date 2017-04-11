class Solution:
    def addBinary(self, a, b):
        if len(a) < len(b):
            a, b = b, a
        carry = 0
        a = a[::-1]
        b = b[::-1]
        tmp = ''
        for i in range(len(a)):
            aa = int(a[i])
            if i >= len(b):
                bb = 0
            else:
                bb = int(b[i])
            tmp += str(aa ^ bb ^ carry)
            if (aa and bb) or (aa and carry) or (bb and carry):
                carry = 1
            else:
                carry = 0
        if carry:
            tmp += '1'
        tmp = tmp[::-1]
        return tmp


a = '111001'
b = '10101'

inst = Solution()
print(inst.addBinary(a, b), bin(int(a, 2) + int(b, 2))[2:])
