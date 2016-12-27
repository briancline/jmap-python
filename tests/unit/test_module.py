import unittest

import jmap


class TestModule(unittest.TestCase):
    def test_module_semantic_version(self):
        ver_info = jmap.VERSION.split('.')
        self.assertGreaterEqual(len(ver_info), 3)
