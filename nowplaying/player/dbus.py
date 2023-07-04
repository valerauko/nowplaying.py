#coding=utf-8

from dbus import Bus, DBusException

BUS = Bus(Bus.TYPE_SESSION)
INTERFACE = 'org.freedesktop.DBus.Properties'
NS = 'org.mpris.MediaPlayer2.'
PLAYER = '/org/mpris/MediaPlayer2'
