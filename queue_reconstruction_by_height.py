class Solution(object):
    def reconstruct_queue(self, people):
        if 0 == len(people):
            return []
        raw_queue = sorted(people, key=lambda p: (-p[0], p[1]))
        queue = []
        for p in raw_queue:
            queue.insert(p[1], p)
        return queue
