# Requires blowfish and zstandard.
# These can be installed by:
# /path/to/python3 -m pip install blowfish zstandard

import sys, blowfish, struct, operator, os, zstandard, math

key = b"\x16\x4B\x7D\x0F\x4F\xA7\x4C\xAC\xD3\x7A\x06\xD9\xF8\x6D\x20\x94"
IV = b"\x9D\x8F\x9D\xA1\x49\x60\xCC\x4C"
cipher = blowfish.Cipher(key, byte_order = "big")
iv = struct.unpack(">Q", IV)
dec_counter = blowfish.ctr_counter(iv[0], f = operator.add)


def processCLE(file_content):
    result = b"".join(cipher.encrypt_ctr(file_content, dec_counter))
    filesize=len(result)
    a = 8*math.ceil(filesize/8) - filesize
    for x in range (a):
        result = result + b"0"
    filesize=len(result)
    result=b"F9BA"+filesize.to_bytes(4,'little')+result

    return result

if __name__ == "__main__":
    # Set current directory
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], 'rb') as decrypted_file:
            encryptedfile = processCLE(decrypted_file.read())
        with open(sys.argv[1]+".encrypted", 'wb') as out:
            out.write(encryptedfile)