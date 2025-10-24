from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import Any, Literal, TypeGuard, overload

def accumulate[T](
    binop: Callable[[T, T], T], seq: Iterable[T], initial: Any = ...
) -> Iterator[T]:
    """
    Repeatedly apply binary function to a sequence, accumulating results

    >>> import cytoolz as cz
    >>> from operator import add, mul
    >>> list(cz.itertoolz.accumulate(add, [1, 2, 3, 4, 5]))
    [1, 3, 6, 10, 15]
    >>> list(cz.itertoolz.accumulate(mul, [1, 2, 3, 4, 5]))
    [1, 2, 6, 24, 120]

    Accumulate is similar to ``reduce`` and is good for making functions like
    cumulative sum:

    >>> from functools import partial, reduce
    >>> sum = partial(reduce, add)
    >>> sum([1, 2, 3, 4, 5])
    15
    >>> cumsum = partial(cz.itertoolz.accumulate, add)
    >>> list(cumsum([1, 2, 3, 4, 5]))
    [1, 3, 6, 10, 15]

    Accumulate also takes an optional argument that will be used as the first
    value. This is similar to reduce.

    >>> list(cz.itertoolz.accumulate(add, [1, 2, 3], -1))
    [-1, 0, 2, 5]
    >>> list(cz.itertoolz.accumulate(add, [], 1))
    [1]

    See Also:
        itertools.accumulate :  In standard itertools for Python 3.2+
    """
    ...

def concat[T](seqs: Iterable[Iterable[T]] | Iterable[T]) -> Iterator[T]:
    """
    Concatenate zero or more iterables, any of which may be infinite.

    An infinite sequence will prevent the rest of the arguments from
    being included.

    We use chain.from_iterable rather than ``chain(*seqs)`` so that seqs
    can be a generator.
    >>> import cytoolz as cz
    >>> list(cz.itertoolz.concat([[], [1], [2, 3]]))
    [1, 2, 3]

    See also:
        itertools.chain.from_iterable  equivalent
    """
    ...

def concatv[T](*seqs: Iterable[T]) -> Iterator[T]:
    """
    Variadic version of concat

    >>> import cytoolz as cz
    >>> list(cz.itertoolz.concatv([], ["a"], ["b", "c"]))
    ['a', 'b', 'c']

    See also:
        itertools.chain
    """
    ...

def cons[T](el: T, seq: Iterable[T]) -> Iterator[T]:
    """
    Add el to beginning of (possibly infinite) sequence seq.

    >>> import cytoolz as cz
    >>> list(cz.itertoolz.cons(1, [2, 3]))
    [1, 2, 3]
    """
    ...

def count(seq: Iterable[Any]) -> int:
    """
    Count the number of items in seq

    >>> import cytoolz as cz
    >>> cz.itertoolz.count([1, 2, 3])
    3

    Like the builtin ``len`` but works on lazy sequences.

    Not to be confused with ``itertools.count``

    See also:
        len
    """
    ...

def diff[T](
    *seqs: Iterable[T], default: T | None = None, key: Callable[[T], Any] | None = None
) -> Iterator[tuple[T, ...]]:
    """
    Return those items that differ between sequences

    >>> import cytoolz as cz
    >>> list(cz.itertoolz.diff([1, 2, 3], [1, 2, 10, 100]))
    [(3, 10)]

    Shorter sequences may be padded with a ``default`` value:

    >>> list(cz.itertoolz.diff([1, 2, 3], [1, 2, 10, 100], default=None))
    [(3, 10), (None, 100)]

    A ``key`` function may also be applied to each item to use during
    comparisons:

    >>> list(cz.itertoolz.diff(["apples", "bananas"], ["Apples", "Oranges"], key=str.lower))
    [('bananas', 'Oranges')]
    """
    ...

def drop[T](n: int, seq: Iterable[T]) -> Iterator[T]:
    """
    The sequence following the first n elements

    >>> import cytoolz as cz
    >>> list(cz.itertoolz.drop(2, [10, 20, 30, 40, 50]))
    [30, 40, 50]

    See Also:
        take
        tail
    """
    ...

def first[T](seq: Iterable[T]) -> T:
    """
    The first element in a sequence

    >>> import cytoolz as cz
    >>> cz.itertoolz.first("ABC")
    'A'
    """
    ...

def frequencies[T](seq: Iterable[T]) -> dict[T, int]:
    """
    Find number of occurrences of each value in seq

    >>> import cytoolz as cz
    >>> cz.itertoolz.frequencies(["cat", "cat", "ox", "pig", "pig", "cat"])
    {'cat': 3, 'ox': 1, 'pig': 2}

    See Also:
        countby
        groupby
    """
    ...

@overload
def get[KT, VT](ind: KT, seq: Mapping[KT, VT], default: Any = ...) -> VT: ...
@overload
def get[T](ind: int, seq: Sequence[T], default: Any = ...) -> T: ...
@overload
def get[KT, VT](
    ind: Iterable[KT], seq: Mapping[KT, VT], default: Any = ...
) -> Iterator[VT]: ...
@overload
def get[T](ind: Iterable[int], seq: Sequence[T], default: Any = ...) -> Iterator[T]: ...
def get(ind: Iterable[int], seq: Sequence[Any], default: Any = ...) -> Iterator[Any]:
    """
    Get element in a sequence or dict

    Provides standard indexing
    >>> import cytoolz as cz
    >>> cz.itertoolz.get(1, 'ABC')       # Same as 'ABC'[1]
    'B'
    >>> cz.itertoolz.get([1, 2], 'ABC')  # ('ABC'[1], 'ABC'[2])
    ('B', 'C')

    Pass a list to get multiple values
    >>> cz.itertoolz.get([1, 2], 'ABC')  # ('ABC'[1], 'ABC'[2])
    ('B', 'C')

    Works on any value that supports indexing/getitem.

    For example here we see that it works with dictionaries
    >>> phonebook = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9999"}
    >>> cz.itertoolz.get('Alice', phonebook)
    '555-1234'

    >>> cz.itertoolz.get(['Alice', 'Bob'], phonebook)
    ('555-1234', '555-5678')

    Provide a default for missing values
    >>> cz.itertoolz.get(['Alice', 'Dennis'], phonebook, None)
    ('555-1234', None)

    See Also:

        pluck
    """
    ...

def groupby[T, K](key: Callable[[T], K] | K, seq: Iterable[T]) -> dict[K, list[T]]:
    """
    Group a collection by a key function

    >>> import cytoolz as cz
    >>> from typing import TypedDict
    >>> names = ["Alice", "Bob", "Charlie", "Dan", "Edith", "Frank"]
    >>> cz.itertoolz.groupby(len, names)
    {3: ['Bob', 'Dan'], 5: ['Alice', 'Edith', 'Frank'], 7: ['Charlie']}
    >>>
    >>> def iseven(x: int) -> bool:
    ...     return x % 2 == 0
    >>> cz.itertoolz.groupby(iseven, [1, 2, 3, 4, 5, 6, 7, 8])
    {False: [1, 3, 5, 7], True: [2, 4, 6, 8]}

    Non-callable keys imply grouping on a member.
    >>> class Person(TypedDict):
    ...     name: str
    ...     gender: str
    >>> data: list[Person] = [
    ...     {"name": "Alice", "gender": "F"},
    ...     {"name": "Bob", "gender": "M"},
    ...     {"name": "Charlie", "gender": "M"},
    ... ]
    >>> result = cz.itertoolz.groupby("gender", data)
    >>> result
    {'F': [{'gender': 'F', 'name': 'Alice'}],
    'M': [{'gender': 'M', 'name': 'Bob'},
        {'gender': 'M', 'name': 'Charlie'}]}

    Not to be confused with ``itertools.groupby``

    See Also:
        countby
    """
    ...

def interleave[T](seqs: Iterable[Iterable[T]]) -> Iterator[T]:
    """
    Interleave a sequence of sequences

    >>> import cytoolz as cz
    >>> list(cz.itertoolz.interleave([[1, 2], [3, 4]]))
    [1, 3, 2, 4]

    >>> "".join(cz.itertoolz.interleave(("ABC", "XY")))
    'AXBYC'

    Both the individual sequences and the sequence of sequences may be infinite

    Returns a lazy iterator
    """
    ...

def interpose[T, E](el: E, seq: Iterable[T]) -> Iterator[T | E]:
    """
    Introduce element between each pair of elements in seq

    >>> import cytoolz as cz
    >>> list(cz.itertoolz.interpose("a", [1, 2, 3]))
    [1, 'a', 2, 'a', 3]
    """
    ...

def isdistinct(seq: Iterable[Any]) -> bool:
    """
    All values in sequence are distinct

    >>> import cytoolz as cz
    >>> cz.itertoolz.isdistinct([1, 2, 3])
    True
    >>> cz.itertoolz.isdistinct([1, 2, 1])
    False

    >>> cz.itertoolz.isdistinct("Hello")
    False
    >>> cz.itertoolz.isdistinct("World")
    True
    """
    ...

def isiterable(x: Any) -> TypeGuard[Iterable[Any]]:
    """
    Is x iterable?

    >>> import cytoolz as cz
    >>> cz.itertoolz.isiterable([1, 2, 3])
    True
    >>> cz.itertoolz.isiterable("abc")
    True
    >>> cz.itertoolz.isiterable(5)
    False
    """
    ...

def iterate[T, T1](func: Callable[[T], T1], x: T) -> Iterator[T1]:
    """
    Repeatedly apply a function func onto an original input

    >>> import cytoolz as cz
    >>> def inc(x: int) -> int:
    ...     return x + 1
    >>> counter = cz.itertoolz.iterate(inc, 0)
    >>> next(counter)
    0
    >>> next(counter)
    1
    >>> next(counter)
    2

    >>> def double(x: int) -> int:
    ...     return x * 2
    >>> powers_of_two = cz.itertoolz.iterate(double, 1)
    >>> next(powers_of_two)
    1
    >>> next(powers_of_two)
    2
    >>> next(powers_of_two)
    4
    >>> next(powers_of_two)
    8
    """
    ...

def join[T1, T2, KT](
    leftkey: Callable[[T1], KT] | KT,
    leftseq: Iterable[T1],
    rightkey: Callable[[T2], KT] | KT,
    rightseq: Iterable[T2],
    left_default: Any = ...,
    right_default: Any = ...,
) -> Iterator[tuple[T1, T2]]:
    """
    Join two sequences on common attributes

    This is a semi-streaming operation.
    - The LEFT sequence is fully evaluated and placed into memory.
    - The RIGHT sequence is evaluated lazily and so can be arbitrarily large.

    Note:
        If right_default is defined, then unique keys of rightseq
        will also be stored in memory.

    >>> import cytoolz as cz
    >>> friends = [
    ...     ("Alice", "Edith"),
    ...     ("Alice", "Zhao"),
    ...     ("Edith", "Alice"),
    ...     ("Zhao", "Alice"),
    ...     ("Zhao", "Edith"),
    ... ]
    >>> cities = [
    ...     ("Alice", "NYC"),
    ...     ("Alice", "Chicago"),
    ...     ("Dan", "Sydney"),
    ...     ("Edith", "Paris"),
    ...     ("Edith", "Berlin"),
    ...     ("Zhao", "Shanghai"),
    ... ]
    >>> # Vacation opportunities
    >>> # In what cities do people have friends?
    >>> result = cz.itertoolz.join(cz.itertoolz.second, friends, cz.itertoolz.first, cities)
    >>> sorted_res = sorted(cz.itertoolz.unique(result))
    >>> [(i[0][0], i[1][1]) for i in sorted_res]
    [
    ('Alice', 'Berlin'),
    ('Alice', 'Paris'),
    ('Alice', 'Shanghai'),
    ('Edith', 'Chicago'),
    ('Edith', 'NYC'),
    ('Zhao', 'Chicago'),
    ('Zhao', 'NYC'),
    ('Zhao', 'Berlin'),
    ('Zhao', 'Paris'),
    ]

    Specify outer joins with keyword arguments ``left_default`` and/or
    ``right_default``.

    Here is a full outer join in which unmatched elements are paired with None.
    >>> list(
    ...     cz.itertoolz.join(
    ...         cz.functoolz.identity,
    ...         [1, 2, 3],
    ...         cz.functoolz.identity,
    ...         [2, 3, 4],
    ...         left_default=None,
    ...         right_default=None,
    ...     )
    ... )
    [(2, 2), (3, 3), (None, 4), (1, None)]

    Usually the key arguments are callables to be applied to the sequences.

    If the keys are not obviously callable then it is assumed that indexing was
    intended, e.g. the following is a legal change.

    The join is implemented as a hash join and the keys of leftseq must be hashable.

    Additionally, if right_default is defined, then keys of rightseq must also be hashable.
    >>> join_res = cz.itertoolz.join(cz.itertoolz.second, friends, cz.itertoolz.first, cities)
    >>> join_head = cz.itertoolz.take(2, join_res)
    >>> list(join_head)
    [(('Edith', 'Alice'), ('Alice', 'NYC')), (('Zhao', 'Alice'), ('Alice', 'NYC'))]
    >>> join_res = cz.itertoolz.join(1, friends, 0, cities)
    >>> head_res = cz.itertoolz.take(2, join_res)
    >>> list(head_res)
    [(('Edith', 'Alice'), ('Alice', 'NYC')), (('Zhao', 'Alice'), ('Alice', 'NYC'))]

    """
    ...

def last[T](seq: Iterable[T]) -> T:
    """
    The last element in a sequence

    >>> import cytoolz as cz
    >>> cz.itertoolz.last("ABC")
    'C'
    """
    ...

def mapcat[T1, T2](
    func: Callable[[Iterable[T1]], Iterable[T2]], seqs: Iterable[Iterable[T1]]
) -> Iterator[T2]:
    """
    Apply func to each sequence in seqs, concatenating results.

    >>> import cytoolz as cz
    >>> list(cz.itertoolz.mapcat(lambda s: [c.upper() for c in s], [["a", "b"], ["c", "d", "e"]]))
    ['A', 'B', 'C', 'D', 'E']
    """
    ...

def merge_sorted[T](
    *seqs: Iterable[T], key: Callable[[T], Any] | None = ...
) -> Iterator[T]:
    """
    Merge and sort a collection of sorted collections

    This works lazily and only keeps one value from each iterable in memory.
    >>> import cytoolz as cz
    >>> list(cz.itertoolz.merge_sorted([1, 3, 5], [2, 4, 6]))
    [1, 2, 3, 4, 5, 6]

    >>> "".join(cz.itertoolz.merge_sorted("abc", "abc", "abc"))
    'aaabbbccc'

    The "key" function used to sort the input may be passed as a keyword.
    >>> list(cz.itertoolz.merge_sorted([2, 3], [1, 3], key=lambda x: x // 3))
    [2, 1, 3, 3]
    """
    ...

def nth[T](n: int, seq: Iterable[T]) -> T:
    """
    The nth element in a sequence

    >>> import cytoolz as cz
    >>> cz.itertoolz.nth(1, "ABC")
    'B'
    """
    ...

@overload
def partition[T](
    n: Literal[1], seq: Iterable[T], pad: None = None
) -> Iterator[tuple[T]]: ...
@overload
def partition[T](
    n: Literal[2], seq: Iterable[T], pad: None = None
) -> Iterator[tuple[T, T]]: ...
@overload
def partition[T](
    n: Literal[3], seq: Iterable[T], pad: None = None
) -> Iterator[tuple[T, T, T]]: ...
@overload
def partition[T](
    n: Literal[4], seq: Iterable[T], pad: None = None
) -> Iterator[tuple[T, T, T, T]]: ...
@overload
def partition[T](
    n: Literal[5], seq: Iterable[T], pad: None = None
) -> Iterator[tuple[T, T, T, T, T]]: ...
@overload
def partition[T](
    n: int, seq: Iterable[T], pad: Any | None = None
) -> Iterator[tuple[T, ...]]: ...
def partition(
    n: int, seq: Iterable[Any], pad: Any | None = None
) -> Iterator[tuple[Any, ...]]:
    """
    Partition sequence into tuples of length n

    >>> import cytoolz as cz
    >>> list(cz.itertoolz.partition(2, [1, 2, 3, 4]))
    [(1, 2), (3, 4)]

    If the length of ``seq`` is not evenly divisible by ``n``, the final tuple
    is dropped if ``pad`` is not specified, or filled to length ``n`` by pad:

    >>> list(cz.itertoolz.partition(2, [1, 2, 3, 4, 5]))
    [(1, 2), (3, 4)]

    >>> list(cz.itertoolz.partition(2, [1, 2, 3, 4, 5], pad=None))
    [(1, 2), (3, 4), (5, None)]

    See Also:
        partition_all
    """
    ...

def partition_all[T](n: int, seq: Iterable[T]) -> Iterator[tuple[T, ...]]:
    """
    Partition all elements of sequence into tuples of length at most n

    The final tuple may be shorter to accommodate extra elements.
    >>> import cytoolz as cz
    >>> list(cz.itertoolz.partition_all(2, [1, 2, 3, 4]))
    [(1, 2), (3, 4)]

    >>> list(cz.itertoolz.partition_all(2, [1, 2, 3, 4, 5]))
    [(1, 2), (3, 4), (5,)]

    See Also:
        partition
    """
    ...

def peek[T](seq: Iterable[T]) -> tuple[T, Iterator[T]]:
    """
    Retrieve the next element of a sequence

    Returns the first element and an iterable equivalent to the original
    sequence, still having the element retrieved.

    >>> import cytoolz as cz
    >>> seq = [0, 1, 2, 3, 4]
    >>> first, seq = cz.itertoolz.peek(seq)
    >>> first
    0
    >>> list(seq)
    [0, 1, 2, 3, 4]
    """
    ...

def peekn[T](n: int, seq: Iterable[T]) -> tuple[tuple[T, ...], Iterator[T]]:
    """
    Retrieve the next n elements of a sequence

    Returns a tuple of the first n elements and an iterable equivalent
    to the original, still having the elements retrieved.
    >>> import cytoolz as cz
    >>> seq = [0, 1, 2, 3, 4]
    >>> first_two, seq = cz.itertoolz.peekn(2, seq)
    >>> first_two
    (0, 1)
    >>> list(seq)
    [0, 1, 2, 3, 4]
    """
    ...

def pluck(
    ind: str | int | list[str] | list[int],
    seqs: Iterable[Sequence[Any] | Mapping[str, Any] | Mapping[int, Any]],
    default: Any = ...,
) -> Iterator[Any]:
    """
    plucks an element or several elements from each item in a sequence.

    ``pluck`` maps ``itertoolz.get`` over a sequence and returns one or more
    elements of each item in the sequence.

    This is equivalent to running `map(curried.get(ind), seqs)`

    ``ind`` can be either a single string/index or a list of strings/indices.
    ``seqs`` should be sequence containing sequences or dicts.

    e.g.

    >>> import cytoolz as cz
    >>> data = [{"id": 1, "name": "Cheese"}, {"id": 2, "name": "Pies"}]
    >>> list(cz.itertoolz.pluck("name", data))
    ['Cheese', 'Pies']
    >>> list(cz.itertoolz.pluck([0, 1], [[1, 2, 3], [4, 5, 7]]))
    [(1, 2), (4, 5)]

    See Also:
        get
        map
    """
    ...

def random_sample[T](
    prob: float, seq: Iterable[T], random_state: Any = ...
) -> Iterator[T]:
    """
    Return elements from a sequence with probability of prob

    Returns a lazy iterator of random items from seq.

    ``random_sample`` considers each item independently and without
    replacement.

    See below how the first time it returned 13 items and the next time it returned 6 items.

    >>> import cytoolz as cz
    >>> seq = list(range(100))
    >>> list(cz.itertoolz.random_sample(0.1, seq)) # doctest: +SKIP
    [6, 9, 19, 35, 45, 50, 58, 62, 68, 72, 78, 86, 95]
    >>> list(cz.itertoolz.random_sample(0.1, seq)) # doctest: +SKIP
    [6, 44, 54, 61, 69, 94]

    Providing an integer seed for ``random_state`` will result in
    deterministic sampling.

    Given the same seed it will return the same sample every time.

    >>> list(cz.itertoolz.random_sample(0.1, seq, random_state=2016)) # doctest: +SKIP
    [7, 9, 19, 25, 30, 32, 34, 48, 59, 60, 81, 98]
    >>> list(cz.itertoolz.random_sample(0.1, seq, random_state=2016)) # doctest: +SKIP
    [7, 9, 19, 25, 30, 32, 34, 48, 59, 60, 81, 98]

    ``random_state`` can also be any object with a method ``random`` that
    returns floats between 0.0 and 1.0 (exclusive).
    >>> from random import Random
    >>> randobj = Random(2016)
    >>> list(cz.itertoolz.random_sample(0.1, seq, random_state=randobj)) # doctest: +SKIP
    [7, 9, 19, 25, 30, 32, 34, 48, 59, 60, 81, 98]
    """
    ...

def reduceby[T, K, VT](
    key: Callable[[T], K] | K,
    binop: Callable[[VT, T], VT],
    seq: Iterable[T],
    init: Any = ...,
) -> dict[K, VT]:
    """
    Perform a simultaneous groupby and reduction

    The computation:
    ```python
    result = reduceby(key, binop, seq, init)
    ```

    is equivalent to the following:
    ```python
    def reduction(group: Iterable[Any]) -> Any:
        return reduce(binop, group, init)

    groups = groupby(key, seq)
    result = valmap(reduction, groups)
    ```
    But the former does not build the intermediate groups, allowing it to
    operate in much less space.  This makes it suitable for larger datasets
    that do not fit comfortably in memory

    The ``init`` keyword argument is the default initialization of the
    reduction.  This can be either a constant value like ``0`` or a callable
    like ``lambda : 0`` as might be used in ``defaultdict``.

    Simple Examples
    ---------------
    >>> import cytoolz as cz
    >>> from operator import add, mul
    >>>
    >>> def iseven(x: int) -> bool:
    ...     return x % 2 == 0
    >>> data = [1, 2, 3, 4, 5]
    >>> cz.itertoolz.reduceby(iseven, add, data)
    {False: 9, True: 6}
    >>> cz.itertoolz.reduceby(iseven, mul, data)
    {False: 15, True: 8}

    Complex Example
    ---------------
    >>> from typing import TypedDict
    >>> class Project(TypedDict):
    ...     name: str
    ...     state: str
    ...     cost: int
    >>> projects: list[Project] = [
    ...     {"name": "build roads", "state": "CA", "cost": 1000000},
    ...     {"name": "fight crime", "state": "IL", "cost": 100000},
    ...     {"name": "help farmers", "state": "IL", "cost": 2000000},
    ...     {"name": "help farmers", "state": "CA", "cost": 200000},
    ... ]
    >>> def acc(accum: int, proj: Project) -> int:
    ...     return accum + proj["cost"]

    >>> cz.itertoolz.reduceby(
    ...     "state",
    ...     acc,
    ...     projects,
    ...     0,
    ... )
    {'CA': 1200000, 'IL': 2100000}

    Example Using ``init``
    ----------------------

    >>> def set_add(s: set[int], i: int) -> set[int]:
    ...     s.add(i)
    ...     return s

    >>> cz.itertoolz.reduceby(iseven, set_add, [1, 2, 3, 4, 1, 2, 3], set)
    {True:  set([2, 4]),
    False: set([1, 3])}
    """
    ...

def remove[T](predicate: Callable[[T], bool], seq: Iterable[T]) -> Iterator[T]:
    """
    Return those items of sequence for which predicate(item) is False

    >>> import cytoolz as cz
    >>> def iseven(x: int) -> bool:
    ...     return x % 2 == 0
    >>> list(cz.itertoolz.remove(iseven, [1, 2, 3, 4]))
    [1, 3]
    """
    ...

def second[T](seq: Iterable[T]) -> T:
    """
    The second element in a sequence

    >>> import cytoolz as cz
    >>> cz.itertoolz.second("ABC")
    'B'
    """
    ...

@overload
def sliding_window[T](n: Literal[1], seq: Iterable[T]) -> Iterator[tuple[T]]: ...
@overload
def sliding_window[T](n: Literal[2], seq: Iterable[T]) -> Iterator[tuple[T, T]]: ...
@overload
def sliding_window[T](n: Literal[3], seq: Iterable[T]) -> Iterator[tuple[T, T, T]]: ...
@overload
def sliding_window[T](
    n: Literal[4], seq: Iterable[T]
) -> Iterator[tuple[T, T, T, T]]: ...
@overload
def sliding_window[T](
    n: Literal[5], seq: Iterable[T]
) -> Iterator[tuple[T, T, T, T, T]]: ...
@overload
def sliding_window[T](n: int, seq: Iterable[T]) -> Iterator[tuple[T, ...]]: ...
def sliding_window(n: int, seq: Iterable[Any]) -> Iterator[tuple[Any, ...]]:
    """
    A sequence of overlapping subsequences

    >>> import cytoolz as cz
    >>> from collections.abc import Sequence
    >>> list(cz.itertoolz.sliding_window(2, [1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4)]

    This function creates a sliding window suitable for transformations like
    sliding means / smoothing

    >>> def mean(seq: Sequence[float]) -> float:
    ...     return float(sum(seq)) / len(seq)
    >>> list(map(mean, cz.itertoolz.sliding_window(2, [1, 2, 3, 4])))
    [1.5, 2.5, 3.5]
    """
    ...

def tail[T](n: int, seq: Iterable[T]) -> list[T]:
    """
    The last n elements of a sequence

    >>> import cytoolz as cz
    >>> cz.itertoolz.tail(2, [10, 20, 30, 40, 50])
    [40, 50]

    See Also:
        drop
        take
    """
    ...

def take[T](n: int, seq: Iterable[T]) -> Iterator[T]:
    """
    The first n elements of a sequence

    >>> import cytoolz as cz
    >>> list(cz.itertoolz.take(2, [10, 20, 30, 40, 50]))
    [10, 20]

    See Also:
        drop
        tail
    """
    ...

def take_nth[T](n: int, seq: Iterable[T]) -> Iterator[T]:
    """
    Every nth item in seq

    >>> import cytoolz as cz
    >>> list(cz.itertoolz.take_nth(2, [10, 20, 30, 40, 50]))
    [10, 30, 50]
    """
    ...

@overload
def topk[T](
    k: Literal[1], seq: Iterable[T], key: Callable[[T], Any] | None = ...
) -> tuple[T]: ...
@overload
def topk[T](
    k: Literal[2], seq: Iterable[T], key: Callable[[T], Any] | None = ...
) -> tuple[T, T]: ...
@overload
def topk[T](
    k: Literal[3], seq: Iterable[T], key: Callable[[T], Any] | None = ...
) -> tuple[T, T, T]: ...
@overload
def topk[T](
    k: Literal[4], seq: Iterable[T], key: Callable[[T], Any] | None = ...
) -> tuple[T, T, T, T]: ...
@overload
def topk[T](
    k: Literal[5], seq: Iterable[T], key: Callable[[T], Any] | None = ...
) -> tuple[T, T, T, T, T]: ...
@overload
def topk[T](
    k: int, seq: Iterable[T], key: Callable[[T], Any] | None = None
) -> tuple[T, ...]: ...
def topk(
    k: int, seq: Iterable[Any], key: Callable[[Any], Any] | None = None
) -> tuple[Any, ...]:
    """
    Find the k largest elements of a sequence

    Operates lazily in ``n*log(k)`` time
    >>> import cytoolz as cz
    >>> cz.itertoolz.topk(2, [1, 100, 10, 1000])
    (1000, 100)
    >>> cz.itertoolz.topk(2, ["Alice", "Bob", "Charlie", "Dan"], key=len)
    ('Charlie', 'Alice')
    >>> cz.itertoolz.topk(3, [5, 1, 5, 3, 7, 9, 7, 5])
    (9, 7, 7)

    See also:
        heapq.nlargest
    """
    ...

def unique[T](seq: Iterable[T], key: Callable[[T], Any] | None = None) -> Iterator[T]:
    """
    Return only unique elements of a sequence

    >>> import cytoolz as cz
    >>> tuple(cz.itertoolz.unique((1, 2, 3)))
    (1, 2, 3)
    >>> tuple(cz.itertoolz.unique((1, 2, 1, 3)))
    (1, 2, 3)

    Uniqueness can be defined by key keyword

    >>> tuple(cz.itertoolz.unique(["cat", "mouse", "dog", "hen"], key=len))
    ('cat', 'mouse')
    """
    ...
