# testSIF = "123456789012"
testSIF = open("input.txt", 'r').read()
layer_count = len(testSIF) // (25 * 6)
layers = []
index = 0
for z in range(layer_count):
    layer = []
    for y in range(6):
        for x in range(25):
            layer += testSIF[index]
            index += 1
    layers.append(layer)

zero = None
low_layer = None

for i in range(len(layers)):
    countzero = layers[i].count("0")
    if zero is None:
        zero = countzero
        low_layer = i
    if countzero < zero:
        zero = countzero
        low_layer = i

print(i, zero, layers[low_layer].count("1") * layers[low_layer].count("2"))
