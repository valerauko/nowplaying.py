#coding=utf-8

from .bluesky import Bluesky
from .misskey import Misskey

class Social:
    @classmethod
    def client(cls, config):
        match config['provider']:
            case 'bluesky':
                return Bluesky(config)
            case 'misskey':
                return Misskey(config)
