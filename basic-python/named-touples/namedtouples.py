from collections import namedtuple

Customer = namedtuple("Customer", "name age")
Customer2 = namedtuple("Cust", ["name", "age"])

print(Customer.__doc__)
print(Customer2.__doc__)

c = Customer("slavo", 33)
c2 = Customer2("jano", 32)

print(c.name);
print(c2.name)



