#!/usr/bin/env python
#coding=utf-8

import sys, os, tweepy, urllib, dbus
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from mastodon import Mastodon

bus = dbus.SessionBus()
folder = os.path.dirname(__file__)+"/nowplaying/"

def _get_dbus_object(path):
	return bus.get_object("org.bansheeproject.Banshee", path)

try:
	obj = _get_dbus_object("/org/bansheeproject/Banshee/PlayerEngine")
	if(str(obj.GetCurrentState()) != "playing"):
		print "died"
		sys.exit(1)
except:
	sys.exit(1)

try:
	obj = _get_dbus_object("/org/bansheeproject/Banshee/PlayerEngine")
	data = obj.GetCurrentTrack()
except:
	sys.exit(1)

if not "artist" in data.keys() or not "name" in data.keys() or not "album" in data.keys():
	sys.exit(1)

twt = u'#nowplaying '+unicode(data["artist"])[:45]+u' - '+unicode(data["name"])[:40]+('...' if len(unicode(data['name'])) > 40 else '')+' ('+unicode(data["album"])[:40]+('...' if len(unicode(data['album'])) > 40 else '')+')'

twt = twt.encode('utf8')

try:
  app = open(folder+"twitter_app.txt","r").read().splitlines()
  auth = tweepy.OAuthHandler(app[0],app[1])
  usr = open(folder+"twitter_user.txt","r").read().splitlines()
  auth.set_access_token(usr[0],usr[1])

  api = tweepy.API(auth)
  api.update_status(status=twt)
except Exception, e:
  print "Twitter error: ", str(e)

try:
  mastodon = Mastodon(client_id=folder+"mastodon_app.txt", access_token=folder+"mastodon_user.txt", api_base_url="https://pawoo.net/") # edit this if needed
  mastodon.toot(twt)
except Exception, e:
  print "Mastodon error: ", str(e)

Notify.init('#nowplaying')
Notify.Notification.new('#nowplaying','#nowplaying sent').show()

sys.exit(0)
