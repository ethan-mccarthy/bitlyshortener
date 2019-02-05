import os
import random
import time

from bitlyshortener import Shortener

tokens = os.getenv('BITLY_TOKENS').strip().split(',')

URLs = [
    'https://arxiv.org/abs/1902.01128v1',
    'https://arxiv.org/abs/1902.01119v1',
    'https://arxiv.org/abs/1902.01080v1',
    'https://arxiv.org/abs/1902.01073v1',
    'https://arxiv.org/abs/1902.01030v1',
    'https://arxiv.org/abs/1902.00916v1',
    'https://arxiv.org/abs/1902.00908v1',
    'https://arxiv.org/abs/1902.00771v1',
    'https://arxiv.org/abs/1902.00719v1',
    'https://arxiv.org/abs/1902.00685v1',
    'https://arxiv.org/abs/1902.00672v1',
    'https://arxiv.org/abs/1902.00659v1',
    'https://arxiv.org/abs/1902.00655v1',
    'https://arxiv.org/abs/1902.00626v1',
    'https://arxiv.org/abs/1902.00624v1',
    'https://arxiv.org/abs/1902.00604v1',
    'https://arxiv.org/abs/1902.00577v1',
    'https://arxiv.org/abs/1902.00541v1',
]

try:
    shortener = Shortener(tokens=tokens)
    urls = random.sample(URLs, k={'none': 0, 'one': 1, 'some': 3, 'all': len(URLs)}['none'])

    print(shortener.shorten_urls(urls))
    print(shortener.shorten_urls(urls[::-1]))

except Exception:
    time.sleep(0.01)  # Delay for longs to flush.
    raise
