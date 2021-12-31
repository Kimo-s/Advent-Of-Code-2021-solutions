
f = open("input.txt", "r")

forwardPos = 0
depth = 0
aim = 0

buf = f.readline()

while buf != '':
    buf = buf.split()
    if buf[0] == "forward":
        forwardPos += int(buf[1])
        depth += aim*int(buf[1])
    elif buf[0] == "down":
        aim += int(buf[1])
    elif buf[0] == "up":
        aim -= int(buf[1])
    buf = f.readline()


print(f"forwad = {forwardPos}, depth = {depth}, Result = {depth*forwardPos}")