class list_ops():
    def __init__(self):
        self = self
    @staticmethod
    def sort_list(list, keyword, reverse=True):
        return sorted(list, key=lambda i: i[keyword], reverse=reverse)

test = list_ops()
