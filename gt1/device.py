from . import command


def _send(func):
    def wrapped(self, *args):
        data = func(self, *args)
        print([hex(a) for a in data])
        self.midi_out.send_message(data)
    return wrapped


class Gt1(object):
    def __init__(self, midi_out):
        self.midi_out = midi_out

    @_send
    def init(self):
        return command.init()

    @_send
    def patch_select(self, patch_number):
        return command.patch_select(patch_number)

