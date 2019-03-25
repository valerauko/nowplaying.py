#!/usr/bin/env python
#coding=utf-8
import sys, os, tweepy, urllib
from dbus import Bus, DBusException
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from mastodon import Mastodon

NS = 'org.mpris.MediaPlayer2.'

bus = Bus(Bus.TYPE_SESSION)
folder = os.path.dirname(__file__)+"/" # edit this if needed

def try_player(name):
  try:
    return bus.get_object(NS + name, '/org/mpris/MediaPlayer2')
  except DBusException as e:
    return False

def get_player():
  players = ['quodlibet', 'clementine', 'spotify']
  for p in players:
    player = try_player(p)
    if player:
      return player
  Exception('No player found')

clem = get_player()
data = clem.Get(NS + 'Player', 'Metadata', dbus_interface = 'org.freedesktop.DBus.Properties')

if not 'xesam:artist' in data.keys() or not 'xesam:title' in data.keys() or not 'xesam:album' in data.keys():
  raise Exception('Wrong data format from player')

twt = u'#nowplaying ' +\
  unicode(', '.join(data['xesam:artist'])) +\
  u' - ' +\
  unicode(data['xesam:title']) +\
  ' (' + unicode(data['xesam:album']) + ')'

# print twt
# sys.exit()

twt = twt.encode('utf8')

app = open(folder + 'twitter_app.txt', 'r').read().splitlines()
auth = tweepy.OAuthHandler(app[0], app[1])
usr = open(folder + 'twitter_user.txt', 'r').read().splitlines()
auth.set_access_token(usr[0], usr[1])

api = tweepy.API(auth)
api.update_status(status = twt)

mastodon = Mastodon(client_id = folder + 'mastodon_app.txt',
                    access_token = folder + 'mastodon_user.txt',
                    api_base_url = 'https://pawoo.net/') # edit this if needed
mastodon.toot(twt)

Notify.init('#nowplaying')
Notify.Notification.new('#nowplaying', '#nowplaying sent').show()

sys.exit(0)
