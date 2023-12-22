"""
TODO:

foo is a function that returns an interger when second argument is 1, returns a string when second argument is 2, returns a list when second argument is 3, otherwise it returns inputs self.
"""
from typing import overload, Literal, Any

@overload
def foo(value, flag: Literal[1]) -> int:
    ...

@overload
def foo(value, flag: Literal[2]) -> str:
    ...

@overload
def foo(value, flag: Literal[3]) -> list:
    ...

@overload
def foo[T](value: T, flag) -> T:
    ...

def foo(value, flag) -> Any:
    ...

