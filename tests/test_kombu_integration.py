import unittest

from kombu.utils.encoding import bytes_to_str
from kombu.serialization import dumps, loads


class KombuIntegrationTests(unittest.TestCase):
    def setUp(self):
        super(KombuIntegrationTests, self).setUp()
        self.message = {
            'title': 'Test Data',
            'nested': {
                'two': 2,
                'bool': False,
            },
        }

    def _kombu_dumps(self, data, serializer):
        return dumps(
            bytes_to_str(data),
            serializer=serializer,
        )

    def _kombu_loads(self, body, content_type, content_encoding):
        return loads(bytes_to_str(body), content_type, content_encoding)

    def _test_serialization(self, serializer):
        content_type, content_encoding, body = self._kombu_dumps(
            self.message,
            serializer,
        )
        unserialized = self._kombu_loads(body, content_type, content_encoding)
        self.assertEqual(
            unserialized,
            self.message,
        )

    def test_json_serialization(self):
        self._test_serialization('fernet_json')

    def test_pickle_serialization(self):
        self._test_serialization('fernet_pickle')

    def test_msgpack_serialization(self):
        self._test_serialization('fernet_msgpack')

    def test_yaml_serialization(self):
        self._test_serialization('fernet_yaml')
