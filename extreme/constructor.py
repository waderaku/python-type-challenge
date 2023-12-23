"""
TODO:

Define a decorator `constructor_parameter` that accepts the type of Foo.
and return a wrapper function with the same signature as the constructor of Foo,
and function decorated by `constructor_parameter` can be called with an instance of Foo.
"""
from typing import Callable
# PはFooのコンストラクタの引数の型
# TはFooの型
# Uは受取る関数の戻り値の型
def constructor_parameter[T, U, **P](cls: Callable[P, T]) -> Callable[[Callable[[T], U]], Callable[P, U]]:
    ...
