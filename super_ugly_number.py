class Solution(object):
    def nth_super_ugly_number(self, n, primes):
        ans = [1]
        indices = [0] * len(primes)
        for _ in range(n - 1):
            cur_min = 2 ** 31
            ids = []
            for i, p in enumerate(primes):
                prod = ans[indices[i]] * p
                if prod < cur_min:
                    cur_min = prod
                    ids = [i]
                elif prod == cur_min:
                    ids.append(i)
            for id_ in ids:
                indices[id_] += 1
            ans.append(cur_min)
        return ans[-1]
