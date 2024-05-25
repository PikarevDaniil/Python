import matplotlib.pyplot as plt
from random import choice

def gen(n):
        heads, tails = 0, 0
        for _ in range(n):
            c = choice((True, False))
            heads += c
            tails += int(not(c))
        return tails, heads

def bell_praph(accurate: int):
    #data_tails = []
    data_heads = []
    for _ in range(accurate):
        chank_size = 100    
        chank = gen(chank_size)
        #data_tails.append(round(chank[0] / chank_size, 2))
        data_heads.append(round(chank[1] / chank_size, 2))

    print(list(filter(lambda x: x < 0.3 or x > 0.7, data_heads)))
    '''ct, ch = {}, {}
    for t, h in zip(data_tails, data_heads):
        if t in ct: ct[t] += 1
        elif t not in ct: ct[t] = 1
        if h in ch: ch[h] += 1
        elif h not in ch: ch[h] = 1''' # for two graphs

    '''ct = {}
    for t in data_tails:
        if t in ct: ct[t] += 1
        else: ct[t] = 1''' # for tails graph

    ch = {}
    for t in data_heads:
        if t in ch: ch[t] += 1
        else: ch[t] = 1   # for heads graph


    #tkeys = list(ct.keys())
    #tvalues = list(ct.values())
    hkeys = list(ch.keys())
    hvalues = list(ch.values())

    win, ax = plt.subplots()
    win.patch.set_facecolor('dimgrey')
    ax.set_facecolor('dimgrey')
    #plt.stem(tkeys, tvalues, 'lightgrey', basefmt=" ")
    plt.stem(hkeys, hvalues, 'black', basefmt="black")
    plt.show()

bell_praph(1_000_000)
