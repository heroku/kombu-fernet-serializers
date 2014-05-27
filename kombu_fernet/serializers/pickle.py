# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from kombu.serialization import pickle, pickle_protocol, unpickle

from . import fernet_encode, fernet_decode

def pickle_dumps(obj, dumper=pickle.dumps):
    return dumper(obj, protocol=pickle_protocol)

MIMETYPE = 'application/x-fernet-python-serialize'

register_args = (
    fernet_encode(pickle_dumps),
    fernet_decode(unpickle),
    MIMETYPE,
    'utf-8',
)
