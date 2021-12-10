with open('day6_1.txt') as file:
    lines = file.readlines()
    jellies = [int(x) for x in lines[0].strip().split(',')]
    for i in range(256):
        for k in range(len(jellies)):
            if (jellies[k] != 0):
                jellies[k] = jellies[k] - 1
            else:
                jellies[k] = 6
                jellies.append(8)
    #print(jellies)
    print(len(jellies))