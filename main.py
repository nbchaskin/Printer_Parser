import pdb

x = 0
t = 0
pos = []


def main():
    text_array = []
    mode = True
    f = open('sample_gcode.txt', 'r')
    for line in f:
        text_array.append(line.split())
    for i in range(len(text_array)):
        if text_array[i][0] == 'G90':
            mode = True
        elif text_array[i][0] == 'G91':
            mode = False
        else:
            pos = parse(text_array[i], mode)
            print(pos)
    f.close()


def parse(line, mode):
    # Can write t as a function of how far x changes though this is a linear model.
    global x, t
    if mode:  # absolute mode
        if line[0] == 'G1':
            x_old = x
            x = float(line[1].split('X')[1])  # x becomes what it is
            # print('x is %f' % x)
            t += abs((x_old - x) / ((float(line[2].split('F')[1])) / 60000))
        if line[0] == 'G4':
            t += float(line[1].split('P')[1])
            # print('t = %f' % t)
    else:
        if line[0] == 'G1':
            x += float(line[1].split('X')[1])  # add to x
            # print('x is %f' % x)
            t += abs(float(line[1].split('X')[1]) / (float(line[2].split('F')[1]) / 60000))
        if line[0] == 'G4':
            t += float(line[1].split('P')[1])
            # print('t = %f' % t)
    return x, t


if __name__ == "__main__":
    main()
