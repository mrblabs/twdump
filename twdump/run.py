import json
import re


import gevent

from oauthlib.oauth1 import SIGNATURE_HMAC, SIGNATURE_TYPE_AUTH_HEADER

from requests_oauthlib import OAuth1
from requests import request


def grep():
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    c_key = '7PcLmmXGswbGVTANJ7MuTQ'
    c_secret = 'IzZWHzQXm9xktB7HfCZdQFwXZOIQU2CkfoJwIHY'
    a_key = '957947294-yUUpRjFkQXQ83ESwRgQDchHCSfdWGEzLsxtd55h2'
    a_secret = 'uzMKB1dNaC99y8gVHS3a5TrMsImYGq5BvwXgto8seHTT3'
    auth = OAuth1(unicode(c_key), unicode(c_secret),
        resource_owner_key=unicode(a_key),
        resource_owner_secret=unicode(a_secret),
        signature_method=SIGNATURE_HMAC,
        signature_type=SIGNATURE_TYPE_AUTH_HEADER)
    headers = {u'User-Agent': u'twdump'}
    while True:
        r = request('post', url,
            auth=auth, headers=headers,
            timeout=5, stream=True,
            **{'params':'locations=37.584229,55.730203,37.65564,55.774256'})
        if r.status_code == 200:
            for line in r.iter_lines():
                if line:
                    data = json.loads(line)
                    text = unicode(data.get('text'))
                    if text:
                        print text
                gevent.sleep(0.)


def main():
    gevent.spawn(grep)

    while True:
        gevent.sleep(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass