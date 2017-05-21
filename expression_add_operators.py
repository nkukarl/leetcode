# TODO: Anything more efficient? Divide and conquer?
class Solution(object):
    def add_operators(self, num, target):
        self.num_combs = set()
        # Split num into groups of numbers so that operators can be inserted
        self.get_num_combs(num, tuple())
        # Get all operator combinations
        all_op_combs = self.get_all_op_combs(len(num) - 1)

        ans = set()
        for num_comb in self.num_combs:
            if 1 == len(num_comb):
                if int(num_comb[0]) == target:
                    ans.add(num_comb)
                continue
            op_combs = all_op_combs[len(num_comb) - 1]
            for op_comb in op_combs:
                expression = num_comb[0] + ''.join(
                    [op + num for op, num in zip(op_comb, num_comb[1:])])
                if eval(expression) == target:
                    ans.add(expression)
        return list(ans)

    def get_num_combs(self, num, cur):
        if '' == num:
            self.num_combs.add(cur)
        else:
            for i in range(len(num)):
                if num[:i + 1].startswith('0') and i > 0:
                    continue
                self.get_num_combs(num[i + 1:], cur + (num[:i + 1],))

    def get_all_op_combs(self, count):
        """
        
        Args:
            count: Maximum number of operators required 

        Returns:
            A dict containing combinations of operators of different numbers

        """
        all_op_combs = {
            1: ['+', '-', '*'],
        }

        for i in range(2, count + 1):
            base_ops = all_op_combs[i - 1]
            cur = []
            for b_p in base_ops:
                for op in ['+', '-', '*']:
                    cur.append(b_p + op)
            all_op_combs[i] = cur

        return all_op_combs
