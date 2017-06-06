class Solution(object):
    def find_duplicate(self, paths):
        summaries = {}
        for path in paths:
            summary = self.summarise_path(path)
            for k, v in summary.items():
                summaries[k] = summaries.get(k, []) + v
        return [v for v in summaries.values() if len(v) > 1]

    def summarise_path(self, path):
        directory, *files = path.split()
        summary = {}
        for file in files:
            filename, content = file[:-1].split('(')
            summary[content] = \
                summary.get(content, []) + [directory + '/' + filename]
        return summary
