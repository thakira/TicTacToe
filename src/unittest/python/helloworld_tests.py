from mockito import mock, verify
import unittest

from helloworld import helloworld

class HelloWorldTest(unittest.TestCase):
    def test_hello_world(self):
        out = mock()

        helloworld(out)

        verify(out).write("Hello World\n")