import main
import unittest

class TestMain(unittest.TestCase):
  def test_print_lib_version(self):
    self.AssertEqual(main.print_lib_version(), "2.18.4")
