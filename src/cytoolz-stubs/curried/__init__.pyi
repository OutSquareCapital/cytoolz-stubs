"""Alternate namespace for cytoolz such that all functions are curried.

Currying provides implicit partial evaluation of all functions

Example:
    Get usually requires two arguments, an index and a collection
    >>> from cytoolz.curried import get
    >>> get(0, ("a", "b"))
    'a'

    When we use it in higher order functions we often want to pass a partially
    evaluated form
    >>> data = [(1, 2), (11, 22), (111, 222)]
    >>> list(map(lambda seq: get(0, seq), data))
    [1, 11, 111]

    The curried version allows simple expression of partial evaluation
    >>> list(map(get(0), data))
    [1, 11, 111]

See Also:
    cytoolz.functoolz.curry
"""

import functools

from .. import dicttoolz as _dt
from .. import functoolz as _ft
from .. import itertoolz as _it
from .. import recipes as rc

accumulate = _ft.curry(_it.accumulate)
assoc = _ft.curry(_dt.assoc)
assoc_in = _ft.curry(_dt.assoc_in)
cons = _ft.curry(_it.cons)
countby = _ft.curry(rc.countby)
dissoc = _ft.curry(_dt.dissoc)
do = _ft.curry(_ft.do)
drop = _ft.curry(_it.drop)
excepts = ...
filter = ...  # noqa: A001
get = _ft.curry(_it.get)
get_in = _ft.curry(_dt.get_in)
groupby = _ft.curry(_it.groupby)
interpose = _ft.curry(_it.interpose)
itemfilter = _ft.curry(_dt.itemfilter)
itemmap = _ft.curry(_dt.itemmap)
iterate = _ft.curry(_it.iterate)
join = _ft.curry(_it.join)
keyfilter = _ft.curry(_dt.keyfilter)
keymap = _ft.curry(_dt.keymap)
map = ...  # noqa: A001
mapcat = _ft.curry(_it.mapcat)
nth = _ft.curry(_it.nth)
partial = _ft.curry(functools.partial)
partition = _ft.curry(_it.partition)
partition_all = _ft.curry(_it.partition_all)
partitionby = _ft.curry(rc.partitionby)
peekn = _ft.curry(_it.peekn)
pluck = _ft.curry(_it.pluck)
random_sample = _ft.curry(_it.random_sample)
reduce = ...
reduceby = _ft.curry(_it.reduceby)
remove = _ft.curry(_it.remove)
sliding_window = _ft.curry(_it.sliding_window)
sorted = ...  # noqa: A001
tail = _ft.curry(_it.tail)
take = _ft.curry(_it.take)
take_nth = _ft.curry(_it.take_nth)
topk = _ft.curry(_it.topk)
unique = _ft.curry(_it.unique)
update_in = _ft.curry(_dt.update_in)
valfilter = _ft.curry(_dt.valfilter)
valmap = _ft.curry(_dt.valmap)
