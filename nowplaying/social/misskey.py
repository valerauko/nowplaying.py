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
        host = urlparse(self.client.meta()['uri']).hostname
        return f'Misskey (@{self.client.i()["username"]}@{host})'
