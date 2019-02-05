# bitlyshortener
**bitlyshortener** is an experimental Python 3.7 based high-volume memory-caching-enabled Bitly V4 URL shortener.
It requires and uses one or more generic access tokens provided by Bitly which it uses semi-randomly.
It is nevertheless limited by per-IP rate limits.
As a disclaimer, this is an unofficial package and it has no association with Bitly.

Expanding a shortened URL and other Bitly operations are outside the scope of this package.

The following are the known rate limits per token:
* Per minute: 100 (presumably for status 200 or 201) [[ref]](https://dev.bitly.com/v4/#section/Rate-Limiting)
* Per hour: 1000 (presumably for status 200 or 201) [[ref]](https://dev.bitly.com/v4/#section/Rate-Limiting) 
* Per month: 10000 (presumably for status 201 only) [[ref] (requires login)](https://app.bitly.com/organization/1/detail)

## Usage
To obtain an access token:
* Sign up for a new Bitly account.
An email address such as `YourGmailUsername+RandomSuffix@gmail.com` should work.
* Verify the email address by clicking the link in the confirmation email.
* In the account profile, navigate to Generic Access Token.
* Enter password and click Generate Token.

To install the package, using Python 3.7+, run:

    pip install bitlyshortener

Usage examples:
```python
from bitlyshortener import Shortener

tokens_pool = ['9fbe2864bb8872f5027c103321ff91be90aea687', '0cbe3864bc8872f5027c103321ff91be30aea787']
shortener = Shortener(tokens=tokens_pool, max_cache_size=8192)

urls = ['https://paperswithcode.com/latest', 'https://towardsdatascience.com/machine-learning/home',
        'https://research.fb.com/publications/']
shortener.shorten_urls(urls)
['https://j.mp/2GhpsxU', 'https://j.mp/2RzN02I', 'https://j.mp/2Gj5TFq']
```

To obtain the fastest response, URLs must be shortened in a batch as in the example above.
A thread pool of up to 32 concurrent requesters is used, but no more than up to five per randomized token.
For example, if two tokens are supplied, up to 2 * 5 = 10 concurrent workers are used.
If eight tokens are supplied, then not 8 * 5 = 40, but a max of 32 concurrent workers are used.
The max limit can, if really necessary, be increased by setting `config.MAX_WORKERS` before initializing the shortener.

Returned short links use the `j.mp` domain with HTTPS.
