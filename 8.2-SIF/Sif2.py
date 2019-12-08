# testSIF = "123456789012"
testSIF = open("input.txt", 'r').read()
# testSIF = "0222112222120000"
x_size = 25
y_size = 6

layer_count = len(testSIF) // (x_size * y_size)
layers = []
index = 0
for z in range(layer_count):
    layer = []
    for y in range(y_size):
        for x in range(x_size):
            layer += testSIF[index]
            index += 1
    layers.append(layer)

print(len(layers) * y_size * x_size)
print(len(testSIF))


def decode_pixel(layers, index):
    color = "2"
    for l in layers:
        if color == "2":
            color = l[index]
    return color


index = 0
for y in range(y_size):
    line = ""
    for x in range(x_size):
        line += ("0" if (decode_pixel(layers, index) == "1") else " ") + " "
        index += 1
    print(line)
