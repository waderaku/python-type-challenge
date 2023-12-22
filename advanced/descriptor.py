"""
TODO:

Create a descriptor and annotate the __get__ method.
"""

from typing import overload, Self
class Descriptor:

    @overload
    def __get__(self, instance: None, owner: type) -> Self:
        """you don't need to implement this"""
        ...
    
    @overload
    def __get__[T](self, instance: T, owner: type[T]) -> str:
        """you don't need to implement this"""
        ...

    def __get__(self, instance, owner) -> Self | str:
        """you don't need to implement this"""
        ...