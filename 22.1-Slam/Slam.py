def stack(deck):
    return deck[::-1]


def cut(deck, position):
    return deck[position:] + deck[:position]


def deal(deck, increment):
    new_deck = [None for _ in deck]
    index = 0
    while index < len(deck):
        new_deck[(index * increment) % len(new_deck)] = deck[index]
        index += 1
    return new_deck


def parser(input, deck):
    out = deck[:]
    for line in input.split("\n"):
        parse = line.split(" ")
        if "stack" in parse:
            out = stack(out)
            # print(out, "stack")
        elif "cut" in parse:
            out = cut(out, int(parse[-1]))
            # print(out, "cut", str(int(parse[-1])))
        elif "increment" in parse:
            out = deal(out, int(parse[-1]))
            # print(out, "deal", str(int(parse[-1])))

    return out


test_input = """deal with increment 7
deal with increment 9
cut -2
"""
cards = [x for x in range(119315717514047)]
shuffle = open("input.txt", "r").read()
for _ in range(101741582076661):
    cards = parser(shuffle, cards)

print(cards[2020])
