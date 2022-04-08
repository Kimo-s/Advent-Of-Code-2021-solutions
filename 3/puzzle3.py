

f = open("input.txt", "r")

buf = f.readline()
input = []
total = 0

freqcancy = [0 for x in range(len(buf))]

while buf != '':
    total += 1
    buf = list(map(lambda x: x, buf))
    if '\n' in buf:
        buf.remove('\n')
    
    freqcancy = list(map(lambda x, y: int(x)+y, buf, freqcancy))

    input.append(buf)
    buf = f.readline()


epsilon_rate = ['1' if x < total/2 else '0' for x in freqcancy]
gamma_rate = ['1' if x > total/2 else '0' for x in freqcancy]

gamma_rate = eval(f"0b{''.join(gamma_rate)}")
epsilon_rate = eval(f"0b{''.join(epsilon_rate)}")

print(f"Gamma rate {gamma_rate} Epsilon {epsilon_rate}. Result {gamma_rate*epsilon_rate}")


oxygan_rate = []

size = len(input[0])
readInput = input.copy()

for i in range(size):
    freq = 0
    for s in range(len(input)):
        if input[s] != 0:
            if int(input[s][i]) == 1:
                freq += 1

    temp = 0
    for ss in range(len(input)):
        if input[ss] != 0:
            temp += 1

    for q in range(len(input)):
        if input[q] == 0:
            continue
        if freq >= temp/2:
            if int(input[q][i]) == 0:
                input[q] = 0
        else:
            if int(input[q][i]) == 1:
                input[q] = 0

    temp = 0
    for ss in range(len(input)):
        if input[ss] != 0:
            temp += 1

    if temp == 1:
        for q in range(len(input)):
            if input[q] != 0:
                oxygan_rate = input[q]
                break
        break
     

input = readInput

CO2_rating = []

for i in range(size):
    freq = 0
    for s in range(len(input)):
        if input[s] != 0:
            if int(input[s][i]) == 1:
                freq += 1

    temp = 0
    for ss in range(len(input)):
        if input[ss] != 0:
            temp += 1

    for q in range(len(input)):
        if input[q] == 0:
            continue
        if freq >= temp/2:
            if int(input[q][i]) == 1:
                input[q] = 0
        else:
            if int(input[q][i]) == 0:
                input[q] = 0
    
    temp = 0
    for ss in range(len(input)):
        if input[ss] != 0:
            temp += 1

    if temp == 1:
        for q in range(len(input)):
            if input[q] != 0:
                CO2_rating = input[q]
                break
        break




oxygan_rate = eval(f"0b{''.join(oxygan_rate)}")
CO2_rating = eval(f"0b{''.join(CO2_rating)}")

print(f"Oxygen {oxygan_rate} and CO2 {CO2_rating}. Answer: {oxygan_rate*CO2_rating}")