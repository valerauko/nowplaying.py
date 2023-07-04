#coding=utf-8

from dbus import DBusException
from .iplayer import IPlayer
from . import dbus

class Clementine(IPlayer):
    @classmethod
    def now(cls):
        try:
            bus = dbus.BUS.get_object(
                dbus.NS + 'clementine', dbus.PLAYER)
            return Clementine(bus)
        except DBusException as _:
            return None
