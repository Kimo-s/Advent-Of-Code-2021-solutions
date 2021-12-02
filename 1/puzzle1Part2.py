if __name__ == "__main__":

    f = open("data.txt", "r")
    theincrease = 0

    buff = f.readline()
    data = []
    while 1:
        if buff == '':
            break
        else:
            data.append(int(buff))
        buff = f.readline()
    f.close()

    calcautedMeasurments = []
    for i in range(len(data)-2):
        calcautedMeasurments.append(sum(data[i:i+3]))

    for i in range(len(calcautedMeasurments)):
        if  calcautedMeasurments[i] > calcautedMeasurments[i-1]:
            theincrease += 1
    
    print(theincrease)