import random
import string


class Codec:
    storage = {}

    def encode(self, longUrl):
        """

        Encodes a URL to a shortened URL.

        """
        shortUrl = self.get_random_string()
        self.storage[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """

        Decodes a shortened URL to its original URL.

        """
        return self.storage.get(shortUrl)

    def get_random_string(self):
        chars = string.ascii_letters + string.digits
        return ''.join(random.sample(chars, 6))
