"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
The decorator takes an argument `message` of type string
"""


from typing import Callable


def decorator[T: Callable](message: str) -> Callable[[T], T]:
    ...

# TODO テストケース足りてないからプルリク出す