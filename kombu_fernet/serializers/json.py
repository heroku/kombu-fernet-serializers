# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import anyjson as _json

from . import fernet_encode, fernet_decode

MIMETYPE = 'application/x-fernet-json'

register_args = (
    fernet_encode(_json.dumps),
    fernet_decode(_json.loads),
    MIMETYPE,
    'utf-8',
)
