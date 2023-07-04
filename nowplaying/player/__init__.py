#coding=utf-8

from .clementine import Clementine
from .quod import Quod
from .spotify import Spotify

class Media:
    @classmethod
    def player(cls, name):
        match name:
            case 'clementine':
                return Clementine.now()
            case 'quod_libet':
                return Quod.now()
            case 'spotify':
                return Spotify.now()
