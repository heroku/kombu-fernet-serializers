# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
from cryptography.fernet import Fernet, InvalidToken

fernet = Fernet(os.environ['KOMBU_FERNET_KEY'])

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
