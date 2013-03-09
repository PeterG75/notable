# vim: set fileencoding=utf-8

# Python imports
from os.path import abspath, join, dirname
import sys
import unittest
import uuid

# Third party imports
from ddt import ddt, data, file_data

# Project imports
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from notable import crypt

@ddt
class TestCrypt(unittest.TestCase):

    def _encrypt(self, content, pwd):
        encrypted = crypt.encrypt(content, pwd)
        self.assertEquals(crypt.decrypt(encrypted, pwd), content)

    @file_data('sample-passwords.json')
    def test_ascii_content_with_password_that_is(self, pwd):
        self._encrypt('abcdefg', pwd)

    @file_data('sample-passwords.json')
    def test_content_containing_newlines_with_password_that_is(self, pwd):
        self._encrypt('abc\nxyz', pwd)

    @file_data('sample-passwords.json')
    def test_content_containing_special_chars_with_password_that_is(self, pwd):
        self._encrypt("""!@#$%^&*()_+_+[]\{}|;':",./<>?""", pwd)

    @unittest.skip("Fix this please in a subsequent commit")
    def test_content_with_unicode_password(self):
        content = 'abcdefg'
        pwd = u"☃"
        encrypted = crypt.encrypt(content, pwd)
        self.assertEquals(crypt.decrypt(encrypted, pwd), content)

if __name__ == '__main__':
    unittest.main()
