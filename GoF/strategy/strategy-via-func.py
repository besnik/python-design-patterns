# Strategy patter using functions

# Context
class Processor:

    def __init__(self, printer):
        self.printer = printer

    def execute(self):
        self.printer()

# Concrete strategy function
def stdout_printer():
    print("Stdout printer")

# Better strategy function
def better_printer():
    print("Better printer")


p1 = Processor(stdout_printer);
p1.execute();

p2 = Processor(better_printer);
p2.execute();