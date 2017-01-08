# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
from cryptography.fernet import Fernet, MultiFernet

fernet = Fernet(os.environ.get('KOMBU_FERNET_KEY') or Fernet.generate_key())
fallback_fernet = None
try:
    fallback_fernet = Fernet(os.environ['KOMBU_FERNET_KEY_PREVIOUS'])
except KeyError:
    pass
else:
    fernet = MultiFernet([fernet, fallback_fernet])


def fernet_encode(func):
    def inner(message):
        return fernet.encrypt(func(message))
    return inner


def fernet_decode(func):
    def inner(encoded_message):
        if isinstance(encoded_message, unicode):
            encoded_message = encoded_message.encode('utf-8')
        message = fernet.decrypt(encoded_message)
        return func(message)
    return inner
