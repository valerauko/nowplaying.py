#coding=utf-8

import misskey
from .isocial import ISocial

class Misskey(ISocial):
    def __init__(self, config):
        self.client = misskey.Misskey(
            config['host'], i = config['token'])

    def post(self, text):
        self.client.notes_create(text = text)
