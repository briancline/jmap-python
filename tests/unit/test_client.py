import unittest

import requests_mock

from jmap import client


class TestClient(unittest.TestCase):
    def test_client_req_is_post(self):
        with requests_mock.Mocker() as mock:
            mock.register_uri(
                'POST', 'mock://host/jmap/api',
                status_code=200,
                json=[['sendTacos', {'sent': True}, '1']])

            c = client.Client('mock://host/jmap/api')
            c.invoke('sendTacos', {'target': 'face'})
            self.assertEqual(mock.call_count, 1)

            req = mock.request_history[0]
            self.assertEqual(req.method, 'POST')

    def test_client_req_json_content_type(self):
        with requests_mock.Mocker() as mock:
            mock.register_uri(
                'POST', 'mock://host/jmap/api',
                status_code=200,
                json=[['sendTacos', {'sent': True}, '1']])

            c = client.Client('mock://host/jmap/api')
            c.invoke('sendTacos', {'target': 'face'})
            self.assertEqual(mock.call_count, 1)

            req = mock.request_history[0]
            self.assertEqual(req.headers.get('Content-Type'),
                             'application/json')

    def test_client_req_user_agent(self):
        with requests_mock.Mocker() as mock:
            mock.register_uri(
                'POST', 'mock://host/jmap/api',
                status_code=200,
                json=[['sendTacos', {'sent': True}, '1']])

            c = client.Client('mock://host/jmap/api')
            c.invoke('sendTacos', {'target': 'face'})
            self.assertEqual(mock.call_count, 1)

            req = mock.request_history[0]
            self.assertTrue(
                req.headers.get('User-Agent').startswith('jmap-python/'))

    def test_client_req_body_single_method(self):
        with requests_mock.Mocker() as mock:
            mock.register_uri(
                'POST', 'mock://host/jmap/api',
                status_code=200,
                json=[['sendTacos', {'sent': True}, '1']])

            c = client.Client('mock://host/jmap/api')
            c.invoke('sendTacos', {'target': 'face'})
            self.assertEqual(mock.call_count, 1)

            req = mock.request_history[0]
            self.assertEqual(req.json(),
                             [['sendTacos', {'target': 'face'}, '1']])

    def test_client_increment_call_id(self):
        with requests_mock.Mocker() as mock:
            mock.register_uri(
                'POST', 'mock://host/jmap/api',
                status_code=200,
                json=[['sendTacos', {'sent': True}, '1']])

            c = client.Client('mock://host/jmap/api')
            c.invoke('sendTacos', {'target': 'face'})
            c.invoke('sendTacos', {'target': 'brian'})
            self.assertEqual(mock.call_count, 2)

            req = mock.request_history[0]
            self.assertEqual(req.json(),
                             [['sendTacos', {'target': 'face'}, '1']])

            req = mock.request_history[1]
            self.assertEqual(req.json(),
                             [['sendTacos', {'target': 'brian'}, '2']])
