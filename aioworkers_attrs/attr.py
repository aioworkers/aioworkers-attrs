import asyncio
import functools

from attr import *  # noqa
import attr
from aioworkers.core.base import AbstractEntity


@attr.s
class _Entity:
    _config = attr.ib(repr=False,)
    _context = attr.ib(repr=False)
    _loop = attr.ib(repr=False)

    @_loop.default
    def default_event_loop(self):
        return asyncio.get_event_loop()

@attr.s
class _AsyncInit:
    async def init(self):
        pass


AbstractEntity.register(_Entity)


def entity(cls):
    for k, v in cls.__dict__.items():
        if hasattr(v, 'init') and isinstance(v.init, bool):
            v.init = False
    result = attr.make_class(cls.__name__, (), bases=(_Entity, attr.s(cls), _AsyncInit))
    return functools.wraps(cls, updated=())(result)


def _filter_private_attr(a, v):
    return not a.name.startswith('_')


asdict = functools.partial(attr.asdict, filter=_filter_private_attr)
