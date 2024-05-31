from icecream import ic
from string import ascii_lowercase as alpha
from random import sample

class enigma:
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
        temp = int(''.join(map(str, self.rpos))) + 1
        temp = tuple(map(int, tuple(str(temp))))
        self.rpos = (0,) * (len(self.rpos) - len(temp)) + temp
    def in_pb(self, char):
        if char in self.pb:
            index = self.pb.index(char)
            char = self.pb[index] if index % 2 else self.pb[index]

    def main(self, msg):
        new_msg = ''
        for i in range(len(msg)):
            char = self.alpha.index(msg[i])
            for r in range(len(self.rot)): char = self.to_ref(char, r)
            char = self.in_ref(char)
            for r in range(len(self.rot))[::-1]: char = self.from_ref(char, r)
            new_msg += self.alpha[char]
            self.in_pb(char)
            self.round_rot()

        return new_msg

# add extra simbols to tha alphabet
alpha += ' '
# generating settings for Enigme machine
rot =tuple(sample(range(len(alpha)), len(alpha)) for _ in range(8))
ref = tuple(sample(range(len(alpha)), len(alpha)))
rot_pos = (0,) * len(rot)
plugs = tuple(sample(range(len(alpha)-10), len(alpha)-10))
# our message
msg = 'hurope i did it'
# creating an Enigma machine 
machine = enigma(alpha, rot, rot_pos, ref, plugs)
# testing the machine
encrypted = machine.main(msg)
# reset the machine settings
machine.rpos = rot_pos
# displaing results
ic(encrypted)
ic(machine.main(encrypted))
