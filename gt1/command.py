import copy
out_message_header = [0xF0, 0x41, 0x00, 0x00, 0x00, 0x00, 0x30, 0x12]
in_message_header = [0xF0, 0x41, 0x00, 0x00, 0x00, 0x00, 0x30, 0x13]

message_footer = [0xF7]


def _calculate_checksum(data):
    base = 0x80
    result = sum(data) % base
    if result != 0:
        result = base - result
    return [result]


def _build_message(data):
    msg = copy.copy(out_message_header)
    msg.extend(data)
    msg.extend(_calculate_checksum(data))
    msg.extend(message_footer)
    return msg


def init():
    return _build_message([0x7F, 0x00, 0x00, 0x01, 0x01])


def patch_select(patch_number):
    return _build_message([0x00, 0x01, 0x00, 0x00, 0x00, patch_number])
