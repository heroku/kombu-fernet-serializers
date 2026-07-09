========================
Kombu Fernet Serializers
========================

This library registers a set of `Kombu`_ serializers which take those built into
Kombu and symmetrically encrypts them using `Fernet`_.

The encryption key is accessed via the `KOMBU_FERNET_KEY` environment variable.
To set the encryption key::

    import os
    from cryptography.fernet import Fernet

    key = Fernet.generate_key()
    os.environ['KOMBU_FERNET_KEY'] = key


To try it out, start a redis server and from the `example` directory, run::

    pip install celery redis
    celery -A tasks worker

Then from another shell::

    python -c "from tasks import add; add.delay(1, 2)"

.. _`Kombu`: http://kombu.readthedocs.org/en/latest/
.. _`Fernet`: http://cryptography.readthedocs.org/en/latest/fernet/
.. _`Celery`: http://celery.readthedocs.org/en/latest/

Contributing
------------

See `CONTRIBUTING.md <CONTRIBUTING.md>`_ for information on how to contribute.

Code of Conduct
---------------

This project adheres to the `Salesforce Open Source Community Code of Conduct <CODE_OF_CONDUCT.md>`_.

Security
--------

Please report any security issue as described in `SECURITY.md <SECURITY.md>`_.

License
-------

Licensed under the Apache License, Version 2.0. See `LICENSE.txt <LICENSE.txt>`_ for details.
