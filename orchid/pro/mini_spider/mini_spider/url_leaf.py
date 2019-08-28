
class url_leaf(object):
    """
    A leaf of Url.
    It has url and its level
    """
    def __init__(self, url="", level=0):
        self.url = url
        self.level = level

    def __str__(self):
        return "{0},{1}".format(self.url, str(self.level))