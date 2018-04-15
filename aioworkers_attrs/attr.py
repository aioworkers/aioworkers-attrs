import asyncio
import functools

from attr import *  # noqa
import attr
from aioworkers.core.base import AbstractEntity


@attr.s
class _Signature:
    _config = attr.ib(repr=False)
    _context = attr.ib(repr=False)
    _loop = attr.ib(repr=False, default=attr.Factory(asyncio.get_event_loop))


class _Entity:
    @property
    def config(self):
        return self._config

    @property
    def context(self):
        return self._context

    def __attrs_post_init__(self):
        if hasattr(self, 'start'):
            self._context.on_start.append(self.start)
        if hasattr(self, 'stop'):
            self._context.on_stop.append(self.stop)

    async def init(self):
        pass


AbstractEntity.register(_Entity)


def entity(cls):
    for k, v in cls.__dict__.items():
        if hasattr(v, 'init') and isinstance(v.init, bool):
            v.init = False
    result = attr.make_class(cls.__name__, (), bases=(_Signature, attr.s(cls), _Entity))
    return functools.wraps(cls, updated=())(result)


def _filter_private_attr(a, v):
    return not a.name.startswith('_')


asdict = functools.partial(attr.asdict, filter=_filter_private_attr)
