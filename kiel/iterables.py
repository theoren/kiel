from __future__ import generator_stop

def drain(iterable):
    """
    Helper method that empties an iterable as it is iterated over.

    Works for:

    * ``dict``
    * ``collections.deque``
    * ``list``
    * ``set``
    """
    if getattr(iterable, "popleft", False):
        def next_item(coll):
            return coll.popleft()
    elif getattr(iterable, "popitem", False):
        def next_item(coll):
            return coll.popitem()
    else:
        def next_item(coll):
            return coll.pop()

    while True:
        try:
            yield next_item(iterable)
        except (IndexError, KeyError):
            return
        # merge from fork https://github.com/denissmirnov/kiel/commit/fa80aa1ccd790c0fbbd8cc46a72162195e1aed69
