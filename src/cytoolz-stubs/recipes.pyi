"""
recipes
========

- countby : Count elements of a collection by a key function
- partitionby : Partition a sequence according to a function
"""

from collections.abc import Callable, Iterable, Iterator
from typing import Any

def countby[T, K](key: Callable[[T], K], seq: Iterable[T]) -> dict[K, int]:
    """
    Count elements of a collection by a key function

    >>> import cytoolz as cz
    >>> cz.recipes.countby(len, ["cat", "mouse", "dog"])
    {3: 2, 5: 1}

    >>> def iseven(x: int) -> bool:
    ...     return x % 2 == 0
    >>> cz.recipes.countby(iseven, [1, 2, 3])
    {True: 1, False: 2}

    See Also:
        groupby
    """
    ...

def partitionby[T](
    func: Callable[[T], Any], seq: Iterable[T]
) -> Iterator[tuple[T, ...]]:
    """Partition a sequence according to a function

    Partition `s` into a sequence of lists such that, when traversing
    `s`, every time the output of `func` changes a new list is started
    and that and subsequent items are collected into that list.

    >>> import cytoolz as cz
    >>> def is_space(c: str) -> bool:
    ...     return c == " "
    >>> list(cz.recipes.partitionby(is_space, "I have space"))
    [('I',), (' ',), ('h', 'a', 'v', 'e'), (' ',), ('s', 'p', 'a', 'c', 'e')]

    >>> def is_large(n: int) -> bool:
    ...     return n > 10
    >>> list(cz.recipes.partitionby(is_large, [1, 2, 1, 99, 88, 33, 99, -1, 5]))
    [(1, 2, 1), (99, 88, 33, 99), (-1, 5)]

    See also:
        partition
        groupby
        itertools.groupby
    """
    ...
