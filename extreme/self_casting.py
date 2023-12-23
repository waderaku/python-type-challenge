"""
TODO:

Fn is a class decorator which takes a callable (`f`).
Fn has a `transform_callable` method, which transform `f` into a different callable,
with an additional Any parameter at the beginning, while preserving the remaining parts
of the function signature.

Note: you're only requried to add type annotations without implementing transform_callable.
"""
from typing import Callable, Concatenate, Any

class Fn[T, **P]:
    def __init__(self, f: Callable[P, T]):
        self.f = f

    def transform_callable(self) -> Callable[Concatenate[Any, P], T]:
        ...
