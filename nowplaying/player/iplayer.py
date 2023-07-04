#coding=utf-8

from .song import Song
from . import dbus

class IPlayer:
    @classmethod
    def now(cls): # -> IPlayer:
        """Returns a IPlayer instance if running or None"""
        pass

    def __init__(self, bus):
        self.bus = bus

    def playing(self): # -> Song:
        """Returns the details of the currently playing song"""
        data = self.bus.Get(
            dbus.NS + 'Player', 'Metadata', dbus_interface = dbus.INTERFACE)
        if data is None:
            return None
        return Song(
            artists = data['xesam:artist'],
            album = data['xesam:album'],
            title = data['xesam:title'])
