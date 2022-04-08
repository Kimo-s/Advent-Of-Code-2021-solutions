

f = open("input.txt", "r")

buf = f.readline()
total = 0

gamma_rate = [0 for x in range(len(buf))]

while buf != '':
    total += 1
    buf = list(map(lambda x: x, buf))
    if '\n' in buf:
        buf.remove('\n')
    
    gamma_rate = list(map(lambda x, y: int(x)+y, buf, gamma_rate))

    buf = f.readline()


epsilon_rate = ['1' if x < total/2 else '0' for x in gamma_rate]
gamma_rate = ['1' if x > total/2 else '0' for x in gamma_rate]

gamma_rate = eval(f"0b{''.join(gamma_rate)}")
epsilon_rate = eval(f"0b{''.join(epsilon_rate)}")

print(gamma_rate*epsilon_rate)
print("test")