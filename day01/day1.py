# part 1
with open('d1input.txt') as file:
    freq = 0
    for line in file:
        freq += int(line)
    print(freq)


# part 2
with open('d1input.txt') as file:
    seq = []
    for line in file:
        seq.append(int(line))

repeat = False
freq = 0
history = {0:1}
while (not repeat):
    for val in seq:
        freq += val
        if (freq in history):
            repeat = True
            break
        else:
            history[freq] = 1
print(f'first repeat: {freq}')
