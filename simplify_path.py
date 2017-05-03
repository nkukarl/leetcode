class Solution(object):
    def simplify_path(self, path):
        stack = []
        for dir in path.split('/'):
            if dir in ['.', '']:
                continue
            if '..' == dir:
                if stack != []:
                    stack.pop()
                continue
            stack.append(dir)
        return '/' + '/'.join(stack)
