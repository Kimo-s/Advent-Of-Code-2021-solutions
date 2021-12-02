if __name__ == "__main__":

    f = open("data.txt", "r")
    theincrease = 0
    last = 0

    buff = f.readline()
    last = int(buff)
    while buff != '':
        if  int(buff) > last:
            theincrease += 1
        last = int(buff)

        buff = f.readline()
    
    f.close()
    print(theincrease)