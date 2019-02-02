from typing import List


class Shortener:
    def __init__(self, *, max_cache_len=512, oauth_tokens: List[str]):
        self._max_cache_len = max_cache_len
        self._oauth_tokens = oauth_tokens

    def shorten(self, urls: List[str]) -> List[str]:
        return urls
