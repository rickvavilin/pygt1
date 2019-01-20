import rtmidi
import codecs
import copy
import time
import gt1

midiout = rtmidi.MidiOut()
midiout.open_port(1)
gt = gt1.Gt1(midiout)
gt.init()
gt.patch_select(1)


midiout.close_port()
del midiout
