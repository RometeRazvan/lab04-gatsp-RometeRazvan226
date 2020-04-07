from GA import GA

def fitness(net, path):
    value = 0
    matrix = net['mat']
    for index in range(0, len(path) - 1):
        node = path[index]
        nextNode = path[index + 1]
        value = value + matrix[node - 1][nextNode - 1]
    value = value + matrix[path[len(path) - 1] - 1][path[0] - 1]
    return value


def readGraph(fileName):
    file = open(fileName, "r")
    net = {}
    n = int(file.readline())
    net['noNodes'] = n
    matrix = []
    for index in range(n):
        matrix.append([])
    index = 0
    line = file.readline()
    while line and index < n:
        args = line.split(",")
        for arg in args:
            matrix[index].append(int(arg))
        index = index + 1
        line = file.readline()
    file.close()
    net['mat'] = matrix
    return net


def main():
    net = readGraph("medium_01_tsp.txt")

    gaParam = {'popSize': 20, 'noGen': 900, 'pc': 0.8, 'pm': 0.1}
    problParam = {'net': net, 'function': fitness, 'noNodes': net['noNodes']}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    ga.oneGenerationElitism()
    final = ga.bestChromosome()
    print(final)


main()
