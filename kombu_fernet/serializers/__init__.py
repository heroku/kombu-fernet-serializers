# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
from cryptography.fernet import Fernet


def lazy_fernet():
    if not hasattr(lazy_fernet, 'fernet'):
        lazy_fernet.fernet = Fernet(os.environ['KOMBU_FERNET_KEY'])
    return lazy_fernet.fernet


def fernet_encode(func):
    def inner(message):
        return lazy_fernet().encrypt(func(message))
    return inner


def fernet_decode(func):
    def inner(encoded_message):
        if isinstance(encoded_message, unicode):
            encoded_message = encoded_message.encode('utf-8')
        message = lazy_fernet().decrypt(encoded_message)
        return func(message)
    return inner
