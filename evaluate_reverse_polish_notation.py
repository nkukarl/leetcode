class Solution(object):
    def eval_rpn(self, tokens):
        stack = []
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: abs(x) // abs(y) * (1 if x * y > 0 else -1),
        }
        for t in tokens:
            if t in ops:
                y, x = stack.pop(), stack.pop()
                stack.append(ops[t](x, y))
            else:
                stack.append(int(t))
        return stack[0] if stack != [] else 0
