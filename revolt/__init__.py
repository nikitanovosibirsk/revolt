from typing import Any

from district42 import GenericSchema

from ._substitutor import Substitutor
from ._version import version

__version__ = version
__all__ = ("substitute", "Substitutor",)

_substitutor = Substitutor()


def substitute(schema: GenericSchema, value: Any, **kwargs: Any) -> Any:
    return schema.__accept__(_substitutor, value=value, **kwargs)
