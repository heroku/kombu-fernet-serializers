# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
key = os.environ['KOMBU_FERNET_KEY']
ttl = os.environ.get('KOMBU_FERNET_TTL', 60)
enforce_ttl = os.environ.get('KOMBU_FERNET_ENFORCE_TTL', '').lower() == 'true'

class InvalidToken(Exception):
    pass

try:
    from cryptography.fernet import Fernet, InvalidToken as CInvalidToken
except ImportError:
    try:
        import fernet
    except ImportError:
        raise RuntimeError("Either cryptography or fernet-py is required")

    fernet.Configuration.enforce_ttl = enforce_ttl
    fernet.Configuration.ttl = ttl

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
            if isinstance(encoded_message, unicode):
                encoded_message = encoded_message.encode('utf-8')
            try:
                message = fernet.decrypt(encoded_message)
            except CInvalidToken:
                raise InvalidToken
            return func(message)
        return inner
