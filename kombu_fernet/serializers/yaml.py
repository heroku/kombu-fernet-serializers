# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from kombu.exceptions import SerializerNotInstalled

from . import fernet_encode, fernet_decode

try:
    import yaml
except ImportError:
    def not_available(*args, **kwargs):
        """In case a client receives a yaml message, but yaml
        isn't installed."""
        raise SerializerNotInstalled(
            'No decoder installed for YAML. Install the PyYAML library')

    yaml_encoder = not_available
    yaml_decoder = None
else:
    yaml_encoder = yaml.safe_dump
    yaml_decoder = yaml.safe_load

MIMETYPE = 'application/x-fernet-yaml'

register_args = (
    fernet_encode(yaml_encoder),
    fernet_decode(yaml_decoder) if yaml_decoder else None,
    MIMETYPE,
    'utf-8',
)
