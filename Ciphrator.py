#__all__ = ['encrypt', 'decrypt']

class Ciphrator:

    def __init__(self):
        self.table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    #def __str__(self):
    #    return 'Base64 Encryptor / Decyptor'

    def encrypt(self, text):
        binarystr = str()
        for c in text:
            binarystr += '{:0>8}'.format(str(bin(ord(c)))[2:])
        while len(binarystr) % 3:
            binarystr += '00000000'
        d = 1
        for i in range(6, len(binarystr) + int(len(binarystr) / 6), 7):
            binarystr = binarystr[:i] + ' ' + binarystr[i:]
        binarystr = binarystr.split(' ')
        if '' in binarystr:
            binarystr.remove('')
        encodedstr = str()
        for b in binarystr:
            if b == '000000':
                encodedstr += '='
            else:
                encodedstr += self.table[int(b, 2)]
        return encodedstr

    def decrypt(self, text):
        binarystr = str()
        for c in text:
            if c == '=':
                binarystr += '000000'
            else:
                binarystr += '{:0>6}'.format(str(bin(self.table.index(c)))[2:])
        for i in range(8, len(binarystr) + int(len(binarystr) / 8), 9):
            binarystr = binarystr[:i] + ' ' + binarystr[i:]
        binarystr = binarystr.split(' ')
        if '' in binarystr:
            binarystr.remove('')
        text = str()
        for b in binarystr:
            if not b == '00000000':
                text += chr(int(b, 2))
        return text
