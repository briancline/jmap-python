import json

import requests

import jmap


CONTENT_TYPE = 'application/json'
USER_AGENT = 'jmap-python/%s' % jmap.VERSION


class Client(object):
    def __init__(self, api_url):
        self.api_url = api_url
        self._method_count = 0

    def _next_id(self):
        """Increment and return a method call ID."""
        self._method_count += 1
        return str(self._method_count)

    def invoke(self, method, args=None, call_id=None):
        """Issue an API request containing one or more method calls."""
        call_id = call_id or self._next_id()
        args = args or {}
        body = json.dumps([
            [method, args, str(call_id)],
        ])
        headers = {
            'Content-Type': CONTENT_TYPE,
            'User-Agent': USER_AGENT,
        }

        return requests.post(self.api_url, data=body, headers=headers)
