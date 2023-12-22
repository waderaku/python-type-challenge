"""
TODO:

foo is a function that returns an interger when called with Foo[int], returns a string when called with Foo[str], otherwise returns a Foo[T].
"""
from typing import overload, Any

class Foo[T]:
    a: T

@overload
def foo(value: Foo[str])-> str:
    ...

@overload
def foo(value: Foo[int]) -> int:
    ...

@overload
def foo[T](value: Foo[T]) -> Foo[T]:
    ...

def foo(value) -> Any:
    ...
