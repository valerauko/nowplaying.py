#coding=utf-8

import misskey
from urllib.parse import urlparse
from .isocial import ISocial

class Misskey(ISocial):
    def __init__(self, config):
        self.client = misskey.Misskey(
            config['host'], i = config['token'])

    def post(self, text):
        self.client.notes_create(text = text)

    def __str__(self):
        host = self.client.address
        user = self.user()
        if user is not None:
            return f'Misskey (@{user}@{host})'
        else:
            return f'Misskey ({host})'

    def user(self):
        try:
            return self.client.i()["username"]
        except Exception as e:
            print(f'Failed to fetch username: {e}')
            print(
                'This tends to happen if the server uses',
                'a Misskey fork such as Foundkey.')
