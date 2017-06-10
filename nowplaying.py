#!/usr/bin/env python
#coding=utf-8

import sys, tweepy, urllib
from dbus import Bus, DBusException
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from mastodon import Mastodon

bus = Bus(Bus.TYPE_SESSION)

def get_clem():
  try:
    return bus.get_object('org.mpris.MediaPlayer2.clementine', '/org/mpris/MediaPlayer2')
  except DBusException as e:
    try:
      return bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
    except DBusException as e:
      print e
      sys.exit(1)

clem = get_clem()
data = clem.Get('org.mpris.MediaPlayer2.Player','Metadata',dbus_interface='org.freedesktop.DBus.Properties')

if not "xesam:artist" in data.keys() or not "xesam:title" in data.keys() or not "xesam:album" in data.keys():
	print "Error."
	sys.exit(1)

str = u'#nowplaying '+unicode(', '.join(data["xesam:artist"]))[:45]+u' - '+unicode(data["xesam:title"])[:40]+('...' if len(unicode(data['xesam:title'])) > 40 else '')+' ('+unicode(data["xesam:album"])[:40]+('...' if len(unicode(data['xesam:album'])) > 40 else '')+')'

#print str
#sys.exit()

str = str.encode('utf8')

try:
    app = open('twitter_app.txt','r').read().splitlines()
	auth = tweepy.OAuthHandler(app[0],app[1])
    usr = open('twitter_user.txt','r').read().splitlines()
	auth.set_access_token(usr[0],usr[1])

	api = tweepy.API(auth)
	api.update_status(status=str)
except TweepError as e:
	print "Twitter error: ", e.strerror

try:
	mastodon = Mastodon(client_id="/home/valerauko/Code/Python/mastodon_app.txt", access_token="/home/valerauko/Code/Python/mastodon_user.txt", api_base_url="https://pawoo.net/")
	mastodon.toot(str)
except:
	print "Mastodon error: ", sys.exec_info()[0]

Notify.init('#nowplaying')
Notify.Notification.new('#nowplaying','#nowplaying sent').show()

sys.exit(0)
