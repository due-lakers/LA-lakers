class R:
    def __init__(self):
        self.code = 0
        self.data = {}
        self.msg = ""

    def ok(self, data):
        self.data = data
        return self

    def error(self, code, msg):
        self.code = code
        self.msg = msg
        return self

