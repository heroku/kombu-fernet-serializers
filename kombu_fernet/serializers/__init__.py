# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
import sys
from cryptography.fernet import Fernet, InvalidToken

PY3 = sys.version_info[0] == 3  # To support Python 3 compatibility

fernet = Fernet(os.environ['KOMBU_FERNET_KEY'])

def fernet_encode(func):
    def inner(message):
        if PY3 and isinstance(message, str):
            message = message.encode('utf-8')
        return fernet.encrypt(func(message))
    return inner

def fernet_decode(func):
    def inner(encoded_message):
        if (PY3 and isinstance(encoded_message, str) or
                isinstance(encoded_message, unicode)):
            encoded_message = encoded_message.encode('utf-8')
        message = fernet.decrypt(encoded_message)
        return func(message)
    return inner
