#!/usr/bin/env python3
#coding=utf-8

import sys

from nowplaying.config import read_config
from nowplaying.notify import notify
from nowplaying.player import Media
from nowplaying.social import Social

config = read_config()

def now_playing():
    for name in config['players'].keys():
        player = Media.player(name)
        if player:
            song = player.playing()
            if song:
                return song

song = now_playing()

if song is None:
    sys.exit(0)

message = f'#nowplaying {song}'

def post_social():
    for social_config in config['social']:
        client = Social.client(social_config)
        if client is not None:
            try:
                client.post(message)
            except Exception as e:
                print(f'Failed to post to {config["provider"]}: {e}')
        else:
            print(f'Malformed social config: {social_config}')

post_social()

if config['notify']:
    notify()
