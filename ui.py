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

class mendelianWin:

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("MendelianUI.glade")
        builder.connect_signals(self)
        window = builder.get_object("winMendelian")

        self.boxAllels = builder.get_object("boxAllels")
        self.labelAllel = builder.get_object("lblAllel")

        self.boxDominant = builder.get_object("boxDominant")
        self.entryDominantA = builder.get_object("txtDominant")

        self.boxDescriptionD = builder.get_object("boxDescriptionD")
        self.entryDescriptionDA = builder.get_object("txtDescriptionD")

        self.boxRecesive = builder.get_object("boxRecesive")
        self.entryRecesiveA = builder.get_object("txtRecesive")

        self.boxDescriptionR = builder.get_object("boxDescriptionR")
        self.entryDescriptionRA = builder.get_object("txtDescriptionR")

        self.spin = builder.get_object("spinFeature")

        self.labelsAllel = []
        self.labelsAllel.append(self.labelAllel)

        self.entriesDominant = []
        self.entriesDominant.append(self.entryDominantA)

        self.entriesDescriptionD = []
        self.entriesDescriptionD.append(self.entryDescriptionDA)

        self.entriesRecesive = []
        self.entriesRecesive.append(self.entryRecesiveA)

        self.entriesDescriptionR = []
        self.entriesDescriptionR.append(self.entryDescriptionRA)

        window.show_all()
        self.characteristics = 0

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print("Hello World!")

    def onSpinChange(self, button):
        print("I'm the fucking spinner")

        if self.spin.get_value_as_int() > self.characteristics:

            labelAllelNew = Gtk.Label()
            labelAllelNew.set_label("----")
            self.labelsAllel.append(labelAllelNew)
            self.boxAllels.pack_end(labelAllelNew, True, True, 1)
            labelAllelNew.show()

            entryDominant = Gtk.Entry()
            self.entriesDominant.append(entryDominant)
            self.boxDominant.pack_end(entryDominant, True, True, 1)
            entryDominant.show()

            entryDescriptionD = Gtk.Entry()
            self.entriesDescriptionD.append(entryDescriptionD)
            self.boxDescriptionD.pack_end(entryDescriptionD, True, True, 1)
            entryDescriptionD.show()

            entryRecesive = Gtk.Entry()
            self.entriesRecesive.append(entryRecesive)
            self.boxRecesive.pack_end(entryRecesive, True, True, 1)
            entryRecesive.show()

            entryDescriptionR = Gtk.Entry()
            self.entriesDescriptionR.append(entryDescriptionR)
            self.boxDescriptionR.pack_end(entryDescriptionR, True, True, 1)
            entryDescriptionR.show()
        else:
            self.boxDominant.remove(self.entriesDominant.pop())
            self.boxDescriptionD.remove(self.entriesDescriptionD.pop())
            self.boxRecesive.remove(self.entriesRecesive.pop())
            self.boxDescriptionR.remove(self.entriesDescriptionR.pop())
            self.boxAllels.remove(self.labelsAllel.pop())
        self.characteristics = self.spin.get_value_as_int()

if __name__=="__main__":
    window = mendelianWin()
    Gtk.main()
