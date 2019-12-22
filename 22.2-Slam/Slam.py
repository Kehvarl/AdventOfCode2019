shuffle = open("input.txt", "r").read()

cards = 119315717514047
position = 2020
shuffles = 101741582076661

a = 1
b = 0

for line in reversed(shuffle.split("\n")):
    parse = line.split(" ")

    if "stack" in parse:
        b += 1
        a *= -1
        b *= -1

    elif "cut" in parse:
        inc = int(parse[-1])
        b += inc
    elif "increment" in parse:
        inc = int(parse[-1])

        p = pow(inc, cards - 2, cards)
        a *= p
        b *= p

    a %= cards
    b %= cards

print((
              pow(a, shuffles, cards) * position +
              b * (pow(a, shuffles, cards) + cards - 1)
              * (pow(a - 1, cards - 2, cards))
      ) % cards)
