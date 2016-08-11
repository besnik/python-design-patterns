# Strategy pattern using functions and replacing externally facing method

import types

class Processor:

    name = "Default processor"

    def __init__(self, f=None):
        if f is not None:
            #self.execute = f # this line is wrong. sets execute as function type, not bound method type
            self.execute = types.MethodType(f, self) # bind function as *method* so self is passes automatically
        pass

    def execute(self):
        print(self.name)

# Concrete strategy function
def exec1(self):
    print("Exec1 processor")


p1 = Processor()
p1.execute();

p2 = Processor(exec1)
p2.execute();

