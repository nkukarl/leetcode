from unittest import TestCase

from encode_and_decode_tinyurl import Codec


class TestCodec(TestCase):
    def test_codec(self):
        # Setup
        codec = Codec()
        url = 'http://www.google.com.au'

        # Exercise
        ans = codec.decode(codec.encode(url))

        # Verify
        self.assertEqual(ans, url)
