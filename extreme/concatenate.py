"""
TODO:

Suppose there's a function `foo`, whose first parameter can be anything.

You want to use `foo`, but want to restrict the first argument to be a `Person`.
You cannot modify `foo`, so you decide to write a function `transform`,
to transform `foo` into the function you want.
"""


from typing import Callable, Concatenate, Any, Protocol


class Person:
    pass


# TODO: 戻り値の型がCallable[[Concatenate[Person, P], T]と定義すると変数名valueに制約出来ない
def transform[T, **P](f: Callable[Concatenate[Person, P], T]) :
    def wrapper(value: Person, *args: P.args, **kwargs: P.kwargs) -> T:
        return f(value, *args, **kwargs)

    return wrapper

def foo2(value, mode: str, *, maybe: bool) -> int:
    return 1

foo_with_person = transform(foo2)

foo_with_person(value=Person(), mode="a", maybe=True)