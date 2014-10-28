# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os

from cryptography.fernet import Fernet, InvalidToken

fernet = Fernet(os.environ['KOMBU_FERNET_KEY'])

def fernet_encode(func):
    def inner(message):
        serialized = func(message)
        if not isinstance(serialized, bytes):
            serialized = serialized.encode('utf-8')
        return fernet.encrypt(serialized)
    return inner

def fernet_decode(func):
    def inner(encoded_message):
        if not isinstance(encoded_message, bytes):
            encoded_message = encoded_message.encode('utf-8')
        message = fernet.decrypt(encoded_message)
        if isinstance(message, bytes):
            message = message.decode('utf-8')
        return func(message)
    return inner
