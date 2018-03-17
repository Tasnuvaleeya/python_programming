from struct import *

# store as byte data
packed_data = pack('iif', 6, 4, 3.95)

# to get bytes data to normal

unpacked_data = unpack('iif', packed_data)
print(unpack('iif', b'\x06\x00\x00\x00\x04\x00\x00\x00\xcd\xcc|@'))
print(unpacked_data)
print(packed_data)
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))
