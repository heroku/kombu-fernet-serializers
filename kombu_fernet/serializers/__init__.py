# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
key = os.environ['KOMBU_FERNET_KEY']

class InvalidToken(Exception):
    pass

try:
    from cryptography.fernet import Fernet, InvalidToken as CInvalidToken
except ImportError:
    try:
        import fernet
    except ImportError:
        raise RuntimeError("Either cryptography or fernet-py is required")

    def fernet_encode(func):
        def inner(message):
            return fernet.generate(key, func(message))
        return inner

    def fernet_decode(func):
        def inner(encoded_message):
            verifier = fernet.verifier(key, encoded_message)
            if verifier.valid():
                return func(verifier.message)
            else:
                raise InvalidToken
        return inner
else:
    fernet = Fernet(key)

    def fernet_encode(func):
        def inner(message):
            return fernet.encrypt(func(message))
        return inner

    def fernet_decode(func):
        def inner(encoded_message):
            try:
                message = fernet.decrypt(encoded_message)
            except CInvalidToken:
                raise InvalidToken
            return func(message)
        return inner
