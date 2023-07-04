#coding=utf-8

from dbus import DBusException
from .iplayer import IPlayer
from . import dbus

class Spotify(IPlayer):
    @classmethod
    def now(cls):
        try:
            bus = dbus.BUS.get_object(
                dbus.NS + 'spotify', dbus.PLAYER)
            return Spotify(bus)
        except DBusException as _:
            return None
