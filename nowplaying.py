#!/usr/bin/env python3
#coding=utf-8
import sys, os, tweepy, urllib
from dbus import Bus, DBusException
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from mastodon import Mastodon

NS = 'org.mpris.MediaPlayer2.'

bus = Bus(Bus.TYPE_SESSION)
folder = os.path.dirname(__file__) + '/nowplaying/' # edit this if needed

def try_player(name):
  try:
    return bus.get_object(NS + name, '/org/mpris/MediaPlayer2')
  except DBusException as e:
    return False

# quod libet is above things so they don't use the mpris key
def try_quod():
  # if quod libet is not running then even just calling the get_object
  # on its key will launch the app which is undesirable. so first check
  # in the dbus name list if quod libet is running
  list = bus.get_object('org.freedesktop.DBus', '/org/freedesktop/DBus').ListNames(
    dbus_interface = 'org.freedesktop.DBus'
  )
  if 'net.sacredchao.QuodLibet' in list:
    return bus.get_object(
      'net.sacredchao.QuodLibet', '/net/sacredchao/QuodLibet'
    )

def get_player():
  players = ['clementine', 'spotify']
  for p in players:
    player = try_player(p)
    if player:
      return player

data = None

quod = try_quod()
if quod is not None and quod.IsPlaying(dbus_interface = 'net.sacredchao.QuodLibet'):
  quod_data = quod.CurrentSong(dbus_interface = 'net.sacredchao.QuodLibet')
  # they even changed the format lol
  data = {
    'xesam:artist': [u'' + quod_data['artist']],
    'xesam:album': u'' + quod_data['album'],
    'xesam:title': u'' + quod_data['title']
  }
else:
  player = get_player()
  if player is None:
    raise Exception('No player found')
  data = player.Get(
    NS + 'Player', 'Metadata',
    dbus_interface = 'org.freedesktop.DBus.Properties'
  )

if not 'xesam:artist' in data.keys() or not 'xesam:title' in data.keys() or not 'xesam:album' in data.keys():
  raise Exception('Unexpected data format from player')

twt = u'#nowplaying ' +\
  ', '.join(data['xesam:artist']) +\
  u' - ' +\
  data['xesam:title'] +\
  ' (' + data['xesam:album'] + ')'

# print twt
# sys.exit()

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
