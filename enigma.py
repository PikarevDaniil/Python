# warning enigma alphabet must be divisible by 2
# otherwise decrypting will be with errors
from icecream import ic
from string import ascii_lowercase as alpha
from random import sample

class Enigma:
    def __init__(self, alpha, rots, rot_pos, ref, plugs):
        self.alpha = alpha
        self.rot = rots
        self.rpos = rot_pos
        self.ref = ref
        self.pb = plugs
    def spec(self, i): return (len(self.alpha) + i) % len(self.alpha)
    def to_ref(self, char, r):
        char = self.spec(char + self.rpos[r])
        char = self.rot[r][char]
        return char
    def in_ref(self, char):
        char = self.spec(char + self.rpos[-1])
        index = self.ref.index(char)
        char = self.ref[self.spec(index-1)] if index % 2 else self.ref[self.spec(index+1)]
        char = self.spec(char - self.rpos[-1])
        return char
    def from_ref(self, char, r):
        char = self.rot[r].index(char)
        char = self.spec(char - self.rpos[r])
        return char
    def round_rot(self):
        self.rpos[0] += 1
        for i in range(1, len(self.rpos)):
            self.rpos[i] += self.rpos[i-1] // len(self.alpha)
            self.rpos[i-1] = self.spec(self.rpos[i-1])
        self.rpos[-1] = self.spec(self.rpos[-1])
    def in_pb(self, char):
        if char in self.pb:
            index = self.pb.index(char)
            char = self.pb[index] if index % 2 else self.pb[index]
        return char
    def main(self, msg):
        new_msg = ''
        old_rot_pos = self.rpos.copy()
        for i in range(len(msg)):
            char = self.alpha.index(msg[i])
            for r in range(len(self.rot)): char = self.to_ref(char, r)
            char = self.in_ref(char)
            for r in range(len(self.rot))[::-1]: char = self.from_ref(char, r)
            char = self.in_pb(char)
            new_msg += self.alpha[char]
            self.round_rot()

        self.rpos = old_rot_pos.copy()
        return new_msg

# add extra symbols to the alphabet
alpha += ' .'

# Constants
ROT = tuple(sample(range(len(alpha)), len(alpha)) for _ in range(1))
REF = tuple(sample(range(len(alpha)), len(alpha)))
ROT_POS = [0] * len(ROT)
PLUGS = tuple(sample(range(len(alpha)-10), len(alpha)-10))
MSG = 'hello'

# creating an Enigma machine 
machine = Enigma(alpha, ROT, ROT_POS, REF, PLUGS)
encrypted = machine.main(MSG)
decrypted = machine.main(encrypted)
ic(encrypted, decrypted)
