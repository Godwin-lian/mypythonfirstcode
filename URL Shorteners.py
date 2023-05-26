"""
URL shortening service using Python.
Users can input a long URL,
and the program will generate a shortened version that
redirects to the original URL.
You can use a database to store the mappings between short and long URLs.
"""

import random
import string


class URLShortener:
    def __init__(self):
        self.urls = {}

    def generate_short_url(self, long_url):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        self.urls[short_url] = long_url
        return short_url

    def redirect_url(self, short_url):
        if short_url in self.urls:
            return self.urls[short_url]
        else:
            return None


# Example usage:
url_shortener = URLShortener()

long_url = "https://www.example.com/some/long/url"
short_url = url_shortener.generate_short_url(long_url)
print(f"Short URL: {short_url}")

redirected_url = url_shortener.redirect_url(short_url)
if redirected_url:
    print(f"Redirected URL: {redirected_url}")
else:
    print("URL not found.")
