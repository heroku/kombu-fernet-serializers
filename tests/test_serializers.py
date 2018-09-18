import unittest

from kombu_fernet.serializers.json import register_args as json_register_args
from kombu_fernet.serializers.msgpack import register_args as msgpack_register_args
from kombu_fernet.serializers.pickle import register_args as pickle_register_args
from kombu_fernet.serializers.yaml import register_args as yaml_register_args


class SerializersTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_json_serializes(self):
        encode = json_register_args[0]
        decode = json_register_args[1]
        data1 = {'value': 'abc123'}
        data2 = decode(encode(data1))
        self.assertEqual(data1, data2)

    def test_msgpack_serializes(self):
        encode = msgpack_register_args[0]
        decode = msgpack_register_args[1]
        data1 = {'value': 'abc123'}
        print('oh hurro', encode(data1))
        data2 = decode(encode(data1))
        self.assertEqual(data1, data2)

    def test_pickle_serializes(self):
        encode = pickle_register_args[0]
        decode = pickle_register_args[1]
        data1 = {'value': 'abc123'}
        data2 = decode(encode(data1))
        self.assertEqual(data1, data2)

    def test_yaml_serializes(self):
        encode = yaml_register_args[0]
        decode = yaml_register_args[1]
        data1 = {'value': 'abc123'}
        data2 = decode(encode(data1))
        self.assertEqual(data1, data2)
