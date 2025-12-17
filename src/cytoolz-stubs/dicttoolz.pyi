"""dicttoolz.

========

- assoc : Return a new dict with new key value pair
- assoc_in : Return a new dict with new, potentially nested, key value pair
- dissoc : Return a new dict with the given key(s) removed.
- get_in : Returns coll[i0][i1]...[iX] where [i0, i1, ..., iX]==keys.
- itemfilter : Filter items in dictionary by item
- itemmap : Apply function to items of dictionary
- keyfilter : Filter items in dictionary by key
- keymap : Apply function to keys of dictionary
- merge : Merge a collection of dictionaries
- merge_with : Merge dictionaries and apply function to combined values
- update_in : Update value in a (potentially) nested dictionary
- valfilter : Filter items in dictionary by value
- valmap : Apply function to values of dictionary
"""

from collections.abc import Callable, Iterable, Mapping, MutableMapping, Sequence
from typing import Any, overload

from typing_extensions import TypeIs

@overload
def assoc[K, V, F: MutableMapping[Any, Any]](
    d: Mapping[K, V],
    key: K,
    value: V,
    *,
    factory: Callable[[], F],
) -> F: ...
@overload
def assoc[K, V](d: Mapping[K, V], key: K, value: V) -> dict[K, V]: ...
def assoc[K, V](d: dict[K, V], key: K, value: V) -> dict[K, V]:
    """Return a new dict with new key value pair.

    New dict has d[key] set to value. Does not modify the initial dictionary.

    >>> import cytoolz as cz
    >>> cz.dicttoolz.assoc({"x": 1}, "x", 2)
    {'x': 2}
    >>> cz.dicttoolz.assoc({"x": 1}, "y", 3)
    {'x': 1, 'y': 3}
    """

@overload
def assoc_in[F: MutableMapping[Any, Any]](
    d: Mapping[Any, Any],
    keys: Sequence[Any],
    value: object,
    *,
    factory: Callable[[], F],
) -> F: ...
@overload
def assoc_in(
    d: Mapping[Any, Any],
    keys: Sequence[Any],
    value: object,
) -> dict[Any, Any]: ...
def assoc_in[K, V](
    d: dict[K, V],
    keys: Iterable[K] | K,
    value: V,
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V]:
    """Return a new dict with new, potentially nested, key value pair.

    >>> import cytoolz as cz
    >>> purchase = {
    ...     "name": "Alice",
    ...     "order": {"items": ["Apple", "Orange"], "costs": [0.50, 1.25]},
    ...     "credit card": "5555-1234-1234-1234",
    ... }
    >>> cz.dicttoolz.assoc_in(purchase, ["order", "costs"], [0.25, 1.00])
    {
        "credit card": "5555-1234-1234-1234",
        "name": "Alice",
        "order": {"costs": [0.25, 1.00], "items": ["Apple", "Orange"]},
    }

    """

@overload
def dissoc[K, V, F: MutableMapping[Any, Any]](
    d: Mapping[K, V],
    *keys: K,
    factory: Callable[[], F],
) -> F: ...
@overload
def dissoc[K, V](
    d: Mapping[K, V],
    *keys: K,
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V]: ...
def dissoc[K, V](
    d: dict[K, V],
    *keys: K,
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V]:
    """Return a new dict with the given key(s) removed.

    New dict has d[key] deleted for each supplied key.
    Does not modify the initial dictionary.

    >>> import cytoolz as cz
    >>> cz.dicttoolz.dissoc({"x": 1, "y": 2}, "y")
    {'x': 1}
    >>> cz.dicttoolz.dissoc({"x": 1, "y": 2}, "y", "x")
    {}
    >>> cz.dicttoolz.dissoc({"x": 1}, "y")  # Ignores missing keys
    {'x': 1}
    """

@overload
def get_in[K, V, D](
    keys: Iterable[K] | K,
    coll: Iterable[V] | Mapping[K, V],
    default: V,
    no_default: bool | None = ...,
) -> V: ...
@overload
def get_in[K, V, D](
    keys: Iterable[K] | K,
    coll: Iterable[V] | Mapping[K, V],
    default: D = ...,
    no_default: bool | None = ...,
) -> V | D: ...
def get_in[K, V](
    keys: Iterable[K] | K,
    coll: Iterable[V] | Mapping[K, V],
    default: Any | None = ...,
    no_default: bool | None = ...,
) -> Any:
    """Returns coll[i0][i1]...[iX] where [i0, i1, ..., iX]==keys.

    If coll[i0][i1]...[iX] cannot be found, returns ``default``, unless
    ``no_default`` is specified, then it raises KeyError or IndexError.

    ``get_in`` is a generalization of ``operator.getitem`` for nested data
    structures such as dictionaries and lists.

    >>> import cytoolz as cz
    >>> transaction = {
    ...     "name": "Alice",
    ...     "purchase": {"items": ["Apple", "Orange"], "costs": [0.50, 1.25]},
    ...     "credit card": "5555-1234-1234-1234",
    ... }
    >>> cz.dicttoolz.get_in(["purchase", "items", 0], transaction)
    'Apple'
    >>> cz.dicttoolz.get_in(["name"], transaction)
    'Alice'
    >>> cz.dicttoolz.get_in(["purchase", "total"], transaction)
    >>> cz.dicttoolz.get_in(["purchase", "items", "apple"], transaction)
    >>> cz.dicttoolz.get_in(["purchase", "items", 10], transaction)
    >>> cz.dicttoolz.get_in(["purchase", "total"], transaction, 0)
    0

    See Also:
        itertoolz.get
        operator.getitem

    """

def itemfilter[K, V](
    predicate: Callable[[tuple[K, V]], bool],
    d: Mapping[K, V],
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V]:
    """Filter items in dictionary by item.

    >>> import cytoolz as cz
    >>> def isvalid(item: tuple[int, int]) -> bool:
    ...     k, v = item
    ...     return k % 2 == 0 and v < 4
    >>> d = {1: 2, 2: 3, 3: 4, 4: 5}
    >>> cz.dicttoolz.itemfilter(isvalid, d)
    {2: 3}

    See Also:
        keyfilter
        valfilter
        itemmap

    """

@overload
def itemmap[K, V, K1, V1, F: MutableMapping[Any, Any]](
    itemfunc: Callable[[tuple[K, V]], tuple[K1, V1]],
    d: Mapping[K, V],
    *,
    factory: Callable[[], F],
) -> F: ...
@overload
def itemmap[K, V, K1, V1](
    itemfunc: Callable[[tuple[K, V]], tuple[K1, V1]],
    d: Mapping[K, V],
) -> dict[K1, V1]: ...
@overload
def itemmap[K, V](func: type[reversed[Any]], d: dict[K, V]) -> dict[V, K]: ...
@overload
def itemmap[K, V, K1, V1](
    func: Callable[[tuple[K, V]], tuple[K1, V1]],
    d: dict[K, V],
) -> dict[K1, V1]: ...
def itemmap[K, V, K1, V1](
    func: Callable[[tuple[K, V]], tuple[K1, V1]] | type[reversed[Any]],
    d: dict[K, V],
) -> dict[K1, V1] | dict[V, K]:
    """Apply function to items of dictionary.

    >>> import cytoolz as cz
    >>> accountids = {"Alice": 10, "Bob": 20}
    >>> cz.dicttoolz.itemmap(reversed, accountids)
    {10: "Alice", 20: "Bob"}

    See Also:
        keymap
        valmap

    """

@overload
def keyfilter[K, V, U](
    predicate: Callable[[K], TypeIs[U]],
    d: Mapping[K, V],
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[U, V]: ...
@overload
def keyfilter[K, V](
    predicate: Callable[[K], bool],
    d: Mapping[K, V],
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V]: ...
def keyfilter[K, V, U](
    predicate: Callable[[K], bool] | Callable[[K], TypeIs[U]],
    d: Mapping[K, V],
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V] | dict[U, V]:
    """Filter items in dictionary by key.

    >>> import cytoolz as cz
    >>> def iseven(x: int) -> bool:
    ...     return x % 2 == 0
    >>> d = {1: 2, 2: 3, 3: 4, 4: 5}
    >>> cz.dicttoolz.keyfilter(iseven, d)
    {2: 3, 4: 5}

    See Also:
        valfilter
        itemfilter
        keymap

    """

@overload
def keymap[K, K1, V](
    keyfunc: Callable[[K], K1],
    d: Mapping[K, V],
    *,
    factory: Callable[[], MutableMapping[K1, V]] = ...,
) -> MutableMapping[K1, V]: ...
@overload
def keymap[K, K1, V](
    keyfunc: Callable[[K], K1],
    d: Mapping[K, V],
) -> dict[K1, V]: ...
def keymap[K, V, K1](
    func: Callable[[K], K1],
    d: dict[K, V],
    factory: Callable[[], dict[K1, V]] = ...,
) -> dict[K1, V]:
    """Apply function to keys of dictionary.

    >>> import cytoolz as cz
    >>> bills = {"Alice": [20, 15, 30], "Bob": [10, 35]}
    >>> cz.dicttoolz.keymap(str.lower, bills)
    {'alice': [20, 15, 30], 'bob': [10, 35]}

    See Also:
        valmap
        itemmap

    """

def merge[K, V](
    *dicts: Mapping[K, V],
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V]:
    """Merge a collection of dictionaries.

    >>> import cytoolz as cz
    >>> cz.dicttoolz.merge({1: "one"}, {2: "two"})
    {1: 'one', 2: 'two'}

    Later dictionaries have precedence
    >>> cz.dicttoolz.merge({1: 2, 3: 4}, {3: 3, 4: 4})
    {1: 2, 3: 3, 4: 4}

    See Also:
        merge_with

    """

def merge_with[K, V](
    func: Callable[[list[V]], V],
    *dicts: Mapping[K, V],
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V]:
    """Merge dictionaries and apply function to combined values.

    A key may occur in more than one dict, and all values mapped from the key
    will be passed to the function as a list, such as func([val1, val2, ...]).

    >>> import cytoolz as cz
    >>> cz.dicttoolz.merge_with(sum, {1: 1, 2: 2}, {1: 10, 2: 20})
    {1: 11, 2: 22}
    >>> cz.dicttoolz.merge_with(cz.itertoolz.first, {1: 1, 2: 2}, {2: 20, 3: 30})
    {1: 1, 2: 2, 3: 30}

    See Also:
        merge

    """

@overload
def update_in[T: Mapping[Any, Any]](
    d: T,
    keys: Sequence[Any],
    func: Callable[[Any], Any],
    default: object | None,
    factory: Callable[[], T],
) -> T: ...
@overload
def update_in[K, V](
    d: dict[K, V],
    keys: Sequence[Any],
    func: Callable[[Any], Any],
    default: object | None,
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V]: ...
@overload
def update_in[K, V, U](
    d: dict[K, V],
    keys: Sequence[Any],
    func: Callable[[Any], Any],
    default: object | None,
    factory: Callable[[], dict[K, U]] = ...,
) -> dict[K, U]: ...
@overload
def update_in[K, V](
    d: dict[K, V],
    keys: Sequence[Any],
    func: Callable[[Any], Any],
    default: object | None = None,
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V]: ...
def update_in(
    d: dict[Any, Any],
    keys: Sequence[Any],
    func: Callable[[Any], Any],
    default: object | None = None,
    factory: Callable[[], dict[Any, Any]] = ...,
) -> dict[Any, Any]:
    """Update value in a (potentially) nested dictionary.

    inputs:
    d - dictionary on which to operate
    keys - list or tuple giving the location of the value to be changed in d
    func - function to operate on that value

    If keys == [k0,..,kX] and d[k0]..[kX] == v, update_in returns a copy of the
    original dictionary with v replaced by func(v), but does not mutate the
    original dictionary.

    If k0 is not a key in d, update_in creates nested dictionaries to the depth
    specified by the keys, with the innermost value set to func(default).

    >>> import cytoolz as cz
    >>> def inc(x: int) -> int:
    ...     return x + 1
    >>> cz.dicttoolz.update_in({"a": 0}, ["a"], inc)
    {'a': 1}

    >>> transaction = {
    ...     "name": "Alice",
    ...     "purchase": {"items": ["Apple", "Orange"], "costs": [0.50, 1.25]},
    ...     "credit card": "5555-1234-1234-1234",
    ... }
    >>> cz.dicttoolz.update_in(transaction, ["purchase", "costs"], sum)
    {'credit card': '5555-1234-1234-1234',
    'name': 'Alice',
    'purchase': {'costs': 1.75, 'items': ['Apple', 'Orange']}}

    >>> # updating a value when k0 is not in d
    >>> cz.dicttoolz.update_in({}, [1, 2, 3], str, default="bar")
    {1: {2: {3: 'bar'}}}
    >>> import cytoolz as cz
    >>> cz.dicttoolz.update_in({1: "foo"}, [2, 3, 4], inc, 0)
    {1: 'foo', 2: {3: {4: 1}}}
    """

@overload
def valfilter[K, V, R](
    predicate: Callable[[V], TypeIs[R]],
    d: Mapping[K, V],
    factory: Callable[[], dict[K, R]] = ...,
) -> dict[K, R]: ...
@overload
def valfilter[K, V](
    predicate: Callable[[V], bool],
    d: Mapping[K, V],
    factory: Callable[[], dict[K, V]] = ...,
) -> dict[K, V]: ...
def valfilter(
    predicate: Callable[[Any], bool],
    d: Mapping[Any, Any],
    factory: Callable[[], dict[Any, Any]] = ...,
) -> dict[Any, Any]:
    """Filter items in dictionary by value.

    >>> import cytoolz as cz
    >>> def iseven(x: int) -> bool:
    ...     return x % 2 == 0
    >>> d: dict[int, int] = {1: 2, 2: 3, 3: 4, 4: 5}
    >>> cz.dicttoolz.valfilter(iseven, d)
    {1: 2, 3: 4}

    See Also:
        keyfilter
        itemfilter
        valmap

    """

@overload
def valmap[K, V, V1](
    valfunc: Callable[[V], V1],
    d: Mapping[K, V],
    *,
    factory: Callable[[], MutableMapping[K, V1]],
) -> MutableMapping[K, V1]: ...
@overload
def valmap[K, V, V1](
    valfunc: Callable[[V], V1],
    d: Mapping[K, V],
) -> dict[K, V1]: ...
def valmap[K, V, V1](
    func: Callable[[V], V1],
    d: dict[K, V],
    factory: Callable[[], dict[Any, Any]] | None = ...,
) -> dict[K, V1]:
    """Apply function to values of dictionary.

    >>> import cytoolz as cz
    >>> bills = {"Alice": [20, 15, 30], "Bob": [10, 35]}
    >>> cz.dicttoolz.valmap(sum, bills)
    {'Alice': 65, 'Bob': 45}

    See Also:
        keymap
        itemmap

    """
