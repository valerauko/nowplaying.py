#coding=utf-8

from argparse import ArgumentParser

parser = ArgumentParser(
    prog = 'nowplaying.py',
    description = 'Script to post what you\'re listening to to social media')

parser.add_argument(
    '-c', '--config',
    default = './config.yaml', dest = 'config',
    help = 'Location of the config file. Default ./config.yaml',
    metavar = 'FILE')

parser.add_argument(
    '--dry-run',
    action = 'store_true', default = False, dest = 'dry_run',
    help = 'if specified, the script won\'t actually post to social media')

def parse_args():
    return parser.parse_args()
