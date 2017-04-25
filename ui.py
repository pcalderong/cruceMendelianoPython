# import gi
# gi.require_version('Gtk', '3.0')
# from gi.repository import Gtk
#
# class MyWindow(Gtk.Window):
#
#     def __init__(self):
#         Gtk.Window.__init__(self, title="Hello World")
#
#         self.button = Gtk.Button(label="Click Here")
#         self.button.connect("clicked", self.on_button_clicked)
#         self.add(self.button)
#
#     def on_button_clicked(self, widget):
#         print("Hello World")
#
# win = MyWindow()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("Proyecto0-a.glade")
builder.connect_signals(Handler())

window = builder.get_object("winMendelian")
window.show_all()

Gtk.main()