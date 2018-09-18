# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from . import fernet_encode, fernet_decode


# NOTE: This package lists this module as an entry point for the group kombu.serializers. Importing
# kombu.serializers before its already been imported elsewhere can raise an ImportError because of a circular
# dependency (kombu.serializers dynamically loads entry points for the group including this one).
def pickle_dumps(*args, **kwargs):
    from kombu.serialization import pickle, pickle_protocol

    def _pickle_dumps(obj, dumper=pickle.dumps):
        return dumper(obj, protocol=pickle_protocol)
    return _pickle_dumps(*args, **kwargs)


def pickle_loads(*args, **kwargs):
    from kombu.serialization import unpickle
    return unpickle(*args, **kwargs)


MIMETYPE = 'application/x-fernet-python-serialize'

register_args = (
    fernet_encode(pickle_dumps),
    fernet_decode(pickle_loads),
    MIMETYPE,
    'utf-8',
)
