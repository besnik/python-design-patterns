# Strategy pattern using OOP and abstract classes (or interface)

from abc import abstractmethod

# Context
class Processor:

    def __init__(self, printer):
        self.printer = printer

    def execute(self):
        self.printer.write()

# Strategy
class AbstractPrinter:

    @abstractmethod
    def write(self):
        '''Writes name on stdout'''

# Concrete strategy
class StdoutPrinter(AbstractPrinter):

    def write(self):
        print("Stdout printer")

# Concrete strategy
class BetterPrinter(AbstractPrinter):
    
    def write(self):
        print("Better printer")


printer = StdoutPrinter()
betterPrinter = BetterPrinter();

p1 = Processor(printer);
p1.execute();

p2 = Processor(betterPrinter);
p2.execute();