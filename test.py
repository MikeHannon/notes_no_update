class Fry(object):
    """docstring for Fry"""
    def __init__(self, arg):
        super(Fry, self).__init__()
        self.arg = arg
        print self.arg


fry = Fry("People")
