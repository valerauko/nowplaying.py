#coding=utf-8

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def notify():
    Notify.init('#nowplaying')
    Notify.Notification.new('#nowplaying', '#nowplaying sent').show()
