#coding=utf-8

from dbus import DBusException
from .iplayer import IPlayer
from . import dbus

INTERFACE = 'net.sacredchao.QuodLibet'

class Quod(IPlayer):
    @classmethod
    def running(cls):
        try:
            list = dbus.BUS.get_object(
                'org.freedesktop.DBus', '/org/freedesktop/DBus').ListNames(
                    dbus_interface = 'org.freedesktop.DBus')
            if INTERFACE in list:
                bus = dbus.BUS.get_object(
                    INTERFACE, '/net/sacredchao/QuodLibet')
                return Quod(bus)
            else:
                return None
        except DBusException as _:
            return None

    def now_playing(self):
        if not self.bus.IsPlaying(dbus_interface = INTERFACE):
            return None
        data = bus.CurrentSong(dbus_interface = INTERFACE)
        return Song(
            artist = data['artist'],
            album = data['album'],
            title = data['title'])
