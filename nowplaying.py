#!/usr/bin/env python3
#coding=utf-8

import sys

from nowplaying.config import read_config
from nowplaying.player import *
from nowplaying.social import *

config = read_config()

PLAYERS = [
    ('clementine', Clementine),
    ('quod_libet', Quod),
    ('spotify', Spotify)]

def now_playing():
    for (key, klass) in PLAYERS:
        if config['players'][key]:
            player = klass.now()
            if player:
                song = player.playing()
                if song:
                    return song

song = now_playing()

if song is None:
    sys.exit(0)

SOCIAL = [
    ('bluesky', Bluesky),
    ('misskey', Misskey)]

message = f'#nowplaying {song}'

def post_social():
    for (key, klass) in SOCIAL:
        social_config = config['social'][key]
        if social_config:
            try:
                social = klass(social_config)
                social.post(message)
                print(f'Posted to {key}')
            except Exception as e:
                print(f'Failed to post to {key}: {e}')

post_social()
