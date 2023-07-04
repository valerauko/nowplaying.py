#!/usr/bin/env python3
#coding=utf-8

import sys

import nowplaying.cli as cli
from nowplaying.config import read_config
from nowplaying.notify import notify
from nowplaying.player import Media
from nowplaying.social import Social

args = cli.parse_args()

config = read_config(path = args.config)

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
                if args.dry_run:
                    print('Not posting because --dry-run was set')
                else:
                    client.post(message)
                print(f'Posted to {client}')
            except Exception as e:
                print(f'Failed to post to {client}: {e}')
        else:
            print(f'Malformed social config: {social_config}')

post_social()

if config['notify']:
    notify()
