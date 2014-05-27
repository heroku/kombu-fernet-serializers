# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from kombu.exceptions import SerializerNotInstalled

from . import fernet_encode, fernet_decode

try:
    try:
        from msgpack import packb as pack, unpackb
        unpack = lambda s: unpackb(s, encoding='utf-8')
    except ImportError:
        # msgpack < 0.2.0 and Python 2.5
        from msgpack import packs as pack, unpacks as unpack  # noqa
except (ImportError, ValueError):

    def not_available(*args, **kwargs):
        """In case a client receives a msgpack message, but msgpack
        isn't installed."""
        raise SerializerNotInstalled(
            'No decoder installed for msgpack. '
            'Please install the msgpack library')
    pack = not_available
    unpack = None

MIMETYPE = 'application/x-fernet-msgpack'

register_args = (
    fernet_encode(pack),
    fernet_decode(unpack) if unpack else None,
    MIMETYPE,
    'utf-8',
)
