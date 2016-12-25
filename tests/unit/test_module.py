import unittest


class TestModule(unittest.TestCase):
    def test_module_import(self):
        import jmap
        self.assertIn('__path__', dir(jmap))
