class list_ops():
    def __init__(self):
        self = self
    @staticmethod
    def sort_list(list, keyword, reverse=True):
        return sorted(list, key=lambda i: i[keyword], reverse=reverse)
    def reverse_dict(dict):
        ret = {y:x for x,y in dict.iteritems()}
       return ret
        

test = list_ops()
