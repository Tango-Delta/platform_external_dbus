#!/usr/bin/env python

import dbus
import dbus.service


import dbus.glib
import pygtk
import gtk

class SomeObject(dbus.service.Object):
    def __init__(self, name):
        dbus.service.Object.__init__(self, "/SomeObject", name)

    @dbus.service.method("org.designfu.SampleInterface")
    def HelloWorld(self, hello_message):
        print (str(hello_message))
        return ["Hello", " from example-service.py"]

    @dbus.service.method("org.designfu.SampleInterface")
    def GetTuple(self):
        return ("Hello Tuple", " from example-service.py")

    @dbus.service.method("org.designfu.SampleInterface")
    def GetDict(self):
        return {"first": "Hello Dict", "second": " from example-service.py"}

session_bus = dbus.SessionBus()
name = dbus.service.Name("org.designfu.SampleService", bus=session_bus)
object = SomeObject(name)

gtk.main()
