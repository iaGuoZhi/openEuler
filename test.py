from cmd import Cmd

n = 1000
files = [0]*n

class Test(Cmd):
    prompt = '> '

    def __init__(self):
        super().__init__()

    def start(self):
        self.cmdloop()

    def do_openmany(self, args=None):
        i = 0
        while i < n:
            try:
                files[i] = open("test.py", "r")
            except OSError as e:
                 print("I/O error({0}): {1}".format(e.errno, e.strerror))
            i += 1

    def do_closemany(self, args=None):
        i = 0
        while i < n:
            files[i].close()
            i += 1

test = Test()
test.start()

