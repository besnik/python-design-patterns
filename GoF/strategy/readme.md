# Strategy Pattern (GoF)

## Pattern description
The pattern decoules client from concrete implementation of a functionality that can change.

## Implementation and Notes
GoF describes the approach to the problem using Abstract classes as a way to provide concrete functionality to the client. Modern static languages provides interfaces structure that could be used as well. Dynamic languages like python can make use of method passing as argument or changing type's interface (by updating method of the type).

 - `strategy-via-classes.py` provides classic implementation via Abstract Classes and abstract method as described in GoF
 - `strategy-via-func` takes advantage of dynamic language and simplifies code
 - `strategy-via-func-ext` does the same except it modifies external interface of the class. Simple assignmnet of function would not work as self parameter would need to be bind to the type so it is automatically populated.
