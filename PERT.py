from math import inf

class Task:
    def __init__(self, id, es=0, ls=inf):
        self.id = id
        self.es = es
        self.ls = ls

    def __str__(self):
        return "Task: "+str(self.id)+", id = "+str(self.id)\
               +", earliest start: "+str(self.es)+", latest start: "+str(self.ls)

    def __gt__(self, other):
        if self.id > other.id:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.id < other.id:
            return True
        else:
            return False

def critical_path(list_of_tasks, graph):

    for i in range(len(list_of_tasks)):
        pom=0
        for j in range(len(list_of_tasks)):
            if graph[j][i] == -inf:
                pom+=1
        if pom == len(list_of_tasks):
            start = list_of_tasks[i]



    for i in range(len(list_of_tasks)):
        pom = True
        for j in range(len(list_of_tasks)):
            if graph[i][j] != -inf:
                pom = False
        if pom == True:
            end = list_of_tasks[i]

    i = start
    dict = {}

    while len(dict) != len(graph):

        dict[i] = search_for_next_tasks(graph, i.id, list_of_tasks)

        for j in dict[i]:
            dict[j]=search_for_next_tasks(graph, j.id, list_of_tasks)

        if dict[i] != []:
            i = dict[i][0]
        else:
            for k in list_of_tasks:
                if k not in dict.keys():
                    i=k

    for i in dict.keys():
        for j in dict[i]:
            if j.es < graph[i.id][j.id]+i.es:
                j.es = i.es + graph[i.id][j.id]

    total_time = end.es
    end.ls = total_time

    pom = end
    while pom != start:
        for i in sorted(dict.keys()):
            if pom in dict[i]:
                if i.ls > pom.ls - graph[i.id][pom.id]:
                    i.ls = pom.ls - graph[i.id][pom.id]
        pom = list_of_tasks[pom.id-1]

    critical_path = []

    for i in dict.keys():
        if i.es == i.ls:
            critical_path.append(i)

    for i in critical_path:
        print(i)

    return critical_path, dict

def search_for_next_tasks(graph, node, list_of_tasks):

    next_tasks = []

    for j in range(len(graph)):
        if graph[node][j] != -inf:
            next_tasks.append(list_of_tasks[j])

    return next_tasks

def define_t(graph):

    t_ij = {}

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != -inf:
                t_ij[(i, j)] = graph[i][j]

    return t_ij

def find_zc(t_ij, list_of_tasks):

    zc = {}

    for i in t_ij.keys():
        for j in list_of_tasks:
            if j.id == i[0]:
                pom1 = j
            elif j.id == i[1]:
                pom2 = j
        zc[i] = pom2.ls - pom1.es - t_ij[i]
    print("Zc: ")
    print(zc)
    print("")

    return zc

def find_zs(t_ij, list_of_tasks):
    zs = {}

    for i in t_ij.keys():
        for j in list_of_tasks:
            if j.id == i[0]:
                pom1 = j
            elif j.id == i[1]:
                pom2 = j
        zs[i] = pom2.ls - pom1.ls - t_ij[i]
    print("Zs: ")
    print(zs)
    print("")

    return zs

def find_zn(t_ij, list_of_tasks):
    zn = {}

    for i in t_ij.keys():
        for j in list_of_tasks:
            if j.id == i[0]:
                pom1 = j
            elif j.id == i[1]:
                pom2 = j
        zn[i] = pom2.es - pom1.ls - t_ij[i]

    print("Zn")
    print(zn)
    print("")

    return zn

def find_pw(t_ij, list_of_tasks):

    pw = {}

    for i in t_ij.keys():
        for j in list_of_tasks:
            if j.id == i[0]:
                pom1 = j
        pw[i] = pom1.es

    print("Pw:")
    print(pw)
    print("")

    return pw

def find_pp(t_ij, list_of_tasks):

    pp = {}

    for i in t_ij.keys():
        for j in list_of_tasks:
            if j.id == i[1]:
                pom1 = j
        pp[i] = pom1.ls - t_ij[i]

    print("Pp:")
    print(pp)
    print("")

    return pp

def find_kw(t_ij, list_of_tasks):

    pw = {}

    for i in t_ij.keys():
        for j in list_of_tasks:
            if j.id == i[0]:
                pom1 = j
        pw[i] = pom1.es + t_ij[i]

    print("Kw:")
    print(pw)
    print("")

    return pw

def find_kp(t_ij, list_of_tasks):

    pp = {}

    for i in t_ij.keys():
        for j in list_of_tasks:
            if j.id == i[1]:
                pom1 = j
        pp[i] = pom1.ls

    print("Pp:")
    print(pp)
    print("")

    return pp

def main():
    A = Task(0)
    B = Task(1)
    C = Task(2)
    D = Task(3)
    E = Task(4)
    F = Task(5)
    G = Task(6)
    H = Task(7)
    I = Task(8)
    J = Task(9)
    K = Task(10)
    L = Task(11)
    M = Task(12)
    list_of_tasks = [A, B, C, D, E, F, G, H, I, J, K, L, M]

    graph = [
        [-inf, 8, 2, 4, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf],
        [-inf, -inf, 4, -inf, 4, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf],
        [-inf, -inf, -inf, -inf, -inf, 1, -inf, -inf, -inf, -inf, -inf, -inf, -inf],
        [-inf, -inf, -inf, -inf, -inf, 7, 9, -inf, -inf, -inf, -inf, -inf, -inf],
        [-inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 7, -inf, -inf, -inf, -inf],
        [-inf, -inf, -inf, -inf, -inf, -inf, 12, 9, -inf, -inf, -inf, -inf, -inf],
        [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 5, 7, -inf],
        [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 3, -inf, -inf],
        [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 1, 5, -inf, -inf],
        [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 6],
        [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 15],
        [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 8],
        [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf],

    ]
    dict = critical_path(list_of_tasks, graph)[1]

    t_ij = define_t(graph)
    print(t_ij)

    find_zc(t_ij, list_of_tasks)

    find_zs(t_ij, list_of_tasks)

    find_zn(t_ij, list_of_tasks)

    find_pw(t_ij, list_of_tasks)

    find_pp(t_ij, list_of_tasks)

    find_kw(t_ij, list_of_tasks)

    find_kp(t_ij, list_of_tasks)

    for i in list_of_tasks:
        print(i)


if __name__ == '__main__':
    main()
