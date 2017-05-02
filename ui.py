import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Pango
from main import main
from utils import getAllels
from mendelian import createPossibleGen
from mendelian import getSinglePhenotype
from utils import readFile
from mendelian import getPhenotypesFromFile

class mendelianWin:


    def __init__(self):
        self.combinationGenotypes =[]
        self.fileCount = 0
        self.fileName = ""
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

        self.dialog = builder.get_object("messageEmptyRow")

        self.boxMom = builder.get_object("boxMom")
        self.boxDad = builder.get_object("boxDad")

        self.fileChooserDialog = builder.get_object("filechooserdialogD")
        self.fileChooserDialog.add_button("Cancel", 1)
        self.fileChooserDialog.add_button("Ok", 2)
        self.fileChooserButton = builder.get_object("fcInput")

        self.labelsAllel = []
        self.labelsAllel.append(self.labelAllel)

        self.entriesDominant = []
        self.entryDominantA.connect("changed", self.onEntryChanged, len(self.entriesDominant))
        self.entriesDominant.append(self.entryDominantA)

        self.entriesDescriptionD = []
        self.entriesDescriptionD.append(self.entryDescriptionDA)

        self.entriesRecesive = []
        self.entriesRecesive.append(self.entryRecesiveA)
        self.entriesDescriptionR = []
        self.entriesDescriptionR.append(self.entryDescriptionRA)

        self.listRadioMom = []
        self.listRadioDad = []

        window.show_all()
        self.characteristics = 0

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print("Hello World!")

    def onEntryChanged(self, entry, index):
        if entry.get_text().isalpha():
            newValue = entry.get_text().upper()
            entry.set_text(newValue)
            self.entriesRecesive[index].set_text(newValue.lower())
            self.labelsAllel[index].set_text(newValue+newValue.lower())
        else:
            entry.set_text("")

    def onFileSelected(self, widget):
        if widget.get_filename():
            self.fileName = widget.get_filename()

    def onResponseDialog(self, widget, response):
        if response == 2:
            print self.fileName
            self.fileChooserButton.set_current_folder("/files")
            text = readFile(self.fileName)
            phenotypes = getPhenotypesFromFile(text)
            self.showPhenotypes(phenotypes)
        else:
            print "No file"

    def restartRadioB(self):
        self.listRadioDad = []
        self.listRadioMom = []
        for c in self.boxDad:
            self.boxDad.remove(c)
        for c in self.boxMom:
            self.boxMom.remove(c)

    def restartUI(self):
        self.labelsAllel = []
        self.entriesDominant = []
        self.entriesDescriptionD = []
        self.entriesRecesive = []
        self.entriesDescriptionR = []
        for c in self.boxAllels:
            self.boxAllels.remove(c)
        for c in self.boxDominant:
            self.boxDominant.remove(c)
        for c in self.boxRecesive:
            self.boxRecesive.remove(c)
        for c in self.boxDescriptionD:
            self.boxDescriptionD.remove(c)
        for c in self.boxDescriptionR:
            self.boxDescriptionR.remove(c)
        labelAllelNew = Gtk.Label()
        self.labelsAllel.append(labelAllelNew)
        self.boxAllels.pack_start(labelAllelNew, True, True, 1)
        labelAllelNew.show()

        entryDominant = Gtk.Entry()
        entryDominant.set_width_chars(1)
        entryDominant.set_max_length(1)
        entryDominant.connect("changed", self.onEntryChanged, len(self.entriesDominant))
        self.entriesDominant.append(entryDominant)
        self.boxDominant.pack_start(entryDominant, True, True, 1)
        entryDominant.show()

        entryDescriptionD = Gtk.Entry()
        self.entriesDescriptionD.append(entryDescriptionD)
        self.boxDescriptionD.pack_start(entryDescriptionD, True, True, 1)
        entryDescriptionD.show()

        entryRecesive = Gtk.Entry()
        entryRecesive.set_width_chars(1)
        entryRecesive.set_max_length(1)
        entryRecesive.set_editable(False)
        self.entriesRecesive.append(entryRecesive)
        self.boxRecesive.pack_start(entryRecesive, True, True, 1)
        entryRecesive.show()

        entryDescriptionR = Gtk.Entry()
        self.entriesDescriptionR.append(entryDescriptionR)
        self.boxDescriptionR.pack_start(entryDescriptionR, True, True, 1)
        entryDescriptionR.show()
        self.spin.set_value(1)

    def showPhenotypes(self, phenotypes):
        self.restartUI()
        for i in phenotypes:
            if i.isupper():
                labelAllelNew = Gtk.Label()
                labelAllelNew.set_text(i+i.lower())
                self.labelsAllel.append(labelAllelNew)
                self.boxAllels.pack_start(labelAllelNew, True, True, 1)
                labelAllelNew.show()

                entryDominant = Gtk.Entry()
                entryDominant.set_width_chars(1)
                entryDominant.set_max_length(1)
                entryDominant.set_text(i)
                entryDominant.connect("changed", self.onEntryChanged, len(self.entriesDominant))
                self.entriesDominant.append(entryDominant)
                self.boxDominant.pack_start(entryDominant, True, True, 1)
                entryDominant.show()

                entryDescriptionD = Gtk.Entry()
                entryDescriptionD.set_text(phenotypes[i])
                self.entriesDescriptionD.append(entryDescriptionD)
                self.boxDescriptionD.pack_start(entryDescriptionD, True, True, 1)
                entryDescriptionD.show()

                entryRecesive = Gtk.Entry()
                entryRecesive.set_width_chars(1)
                entryRecesive.set_max_length(1)
                entryRecesive.set_editable(False)
                entryRecesive.set_text(i.lower())
                self.entriesRecesive.append(entryRecesive)
                self.boxRecesive.pack_start(entryRecesive, True, True, 1)
                entryRecesive.show()

                entryDescriptionR = Gtk.Entry()
                entryDescriptionR.set_text(phenotypes[i.lower()])
                self.entriesDescriptionR.append(entryDescriptionR)
                self.boxDescriptionR.pack_start(entryDescriptionR, True, True, 1)
                entryDescriptionR.show()
        total = len(phenotypes)
        self.entryDominantA.hide()
        self.entryDescriptionDA.hide()
        self.labelAllel.hide()
        self.entriesDescriptionR.hide()
        self.entriesDescriptionD.hide()
        self.spin.set_value(total/2)

    def onOkPressed(self, widget):
        self.dialog.hide()

    def onClearClicked(self, widget):
        self.restartRadioB()
        self.restartUI()

    def onExecutePressefd(self, button):
        getMom = ""
        getDad = ""
        self.listRadioMom.pop(0)
        self.listRadioDad.pop(0)
        for gM in self.listRadioMom:
            if gM.get_active():
                getMom = gM.get_label()
        for gD in self.listRadioDad:
            if gD.get_active():
                getDad = gD.get_label()
        hashCharacteristics = self.getCharacteristics()
        main(getDad, getMom, hashCharacteristics, False)

    def getCharacteristics(self):
        hashCharacteristics = {}
        for i in range(len(self.entriesDominant)):
            hashCharacteristics[self.entriesDominant[i].get_text()] = self.entriesDescriptionD[i].get_text()
            hashCharacteristics[self.entriesRecesive[i].get_text()] = self.entriesDescriptionR[i].get_text()
        return hashCharacteristics

    def onExportClicked(self, button):
        hashCharacteristics = self.getCharacteristics()
        file = open("files/newCharacteristics"+str(self.fileCount)+".txt", "w")
        self.fileCount += 1
        file.write("Phenotypes\n")
        file.write("==========\n")
        for h in hashCharacteristics:
            file.write(h+" = "+hashCharacteristics[h]+"\n")
        file.close()

    def onGenParentsPressed(self, button):
        labels = getAllels(self.labelsAllel)
        self.restartRadioB()
        hashCharacteristics = {}
        for i in range(len(self.entriesDominant)):
            hashCharacteristics[self.entriesDominant[i].get_text()] = self.entriesDescriptionD[i].get_text()
            hashCharacteristics[self.entriesRecesive[i].get_text()] = self.entriesDescriptionR[i].get_text()
        self.combinationGenotypes = createPossibleGen(labels)
        lblMom = Gtk.Label("Mom")
        lblDad = Gtk.Label("Dad")
        context = lblMom.create_pango_context()
        font_description = context.get_font_description()
        increase = 14
        font_size = 1024*increase
        font_description.set_size(font_size)
        lblMom.override_font(font_description)
        lblDad.override_font(font_description)
        self.listRadioMom.append(lblMom)
        self.listRadioDad.append(lblDad)
        self.boxDad.pack_start(lblDad, True, True, 0)
        self.boxMom.pack_start(lblMom, True, True, 0)
        lblMom.show()
        lblDad.show()
        radioMom = Gtk.RadioButton(label="GroupMom")
        radioDad = Gtk.RadioButton(label="GroupDad")
        for c in self.combinationGenotypes:
            rbMom = Gtk.RadioButton.new_from_widget(radioMom)
            rbMom.set_label(c)
            rbMom.set_tooltip_markup(getSinglePhenotype(c, hashCharacteristics))
            rbDad = Gtk.RadioButton.new_from_widget(radioDad)
            rbDad.set_label(c)
            rbDad.set_tooltip_markup(getSinglePhenotype(c, hashCharacteristics))
            self.listRadioDad.append(rbDad)
            self.listRadioMom.append(rbMom)
            self.boxMom.pack_start(rbMom, True, True, 0)
            self.boxDad.pack_start(rbDad, True, True, 0)
            rbMom.show()
            rbDad.show()

    def onSpinChange(self, button):
        index = len(self.entriesDominant) - 1
        lastEntryDominant = self.entriesDominant[index].get_text()
        lastEntryDescriptionD = self.entriesDominant[index].get_text()
        lastEntryDescriptionR = self.entriesDominant[index].get_text()
        if (not lastEntryDominant == "") and (not lastEntryDescriptionD == "") and (not lastEntryDescriptionR == ""):
            if self.spin.get_value_as_int() > self.characteristics:
                labelAllelNew = Gtk.Label()
                self.labelsAllel.append(labelAllelNew)
                self.boxAllels.pack_start(labelAllelNew, True, True, 1)
                labelAllelNew.show()

                entryDominant = Gtk.Entry()
                entryDominant.set_width_chars(1)
                entryDominant.set_max_length(1)
                entryDominant.connect("changed", self.onEntryChanged, len(self.entriesDominant))
                self.entriesDominant.append(entryDominant)
                self.boxDominant.pack_start(entryDominant, True, True, 1)
                entryDominant.show()

                entryDescriptionD = Gtk.Entry()
                self.entriesDescriptionD.append(entryDescriptionD)
                self.boxDescriptionD.pack_start(entryDescriptionD, True, True, 1)
                entryDescriptionD.show()

                entryRecesive = Gtk.Entry()
                entryRecesive.set_width_chars(1)
                entryRecesive.set_max_length(1)
                entryRecesive.set_editable(False)
                self.entriesRecesive.append(entryRecesive)
                self.boxRecesive.pack_start(entryRecesive, True, True, 1)
                entryRecesive.show()

                entryDescriptionR = Gtk.Entry()
                self.entriesDescriptionR.append(entryDescriptionR)
                self.boxDescriptionR.pack_start(entryDescriptionR, True, True, 1)
                entryDescriptionR.show()
            else:
                self.boxDominant.remove(self.entriesDominant.pop())
                self.boxDescriptionD.remove(self.entriesDescriptionD.pop())
                self.boxRecesive.remove(self.entriesRecesive.pop())
                self.boxDescriptionR.remove(self.entriesDescriptionR.pop())
                self.boxAllels.remove(self.labelsAllel.pop())
        else:
            self.spin.set_value(self.characteristics)
            self.dialog.show()
        self.characteristics = self.spin.get_value_as_int()

if __name__=="__main__":
    window = mendelianWin()
    Gtk.main()
