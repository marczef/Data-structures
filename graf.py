#!/usr/bin/python
# -*- coding: utf-8 -*-

import polska
import math

class Edge:
    pass

class Vertex:
    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.key == other.key:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

class Matrix:

    def __init__(self):
        self.vertex = []
        self.edge = []
        self.matrix = []
        self.dict = {}

    def insertVertex(self, vertex):

        self.vertex.append(vertex)
        self.dict[vertex.key] = len(self.matrix)

        if self.matrix == []:
            self.matrix.append([0])

        else:
            self.matrix.append([0 for i in range(len(self.vertex))])
            for i in range(len(self.vertex)-1):
                self.matrix[i].append(0)

    def insertEdge(self, vertex1, vertex2, edge=1):

        self.edge.append([vertex1, vertex2])

        self.matrix[self.dict[vertex1.key]][self.dict[vertex2.key]] = 1

    def deleteVertex(self, vertex):

        pom=self.dict[vertex.key]

        self.vertex.remove(vertex)

        for i in range(len(self.edge)-1, -1, -1):
            if vertex in self.edge[i]:
                del self.edge[i]

        for i in range(len(self.matrix)):
            del self.matrix[i][self.dict[vertex.key]]

        del self.matrix[self.dict[vertex.key]]

        del self.dict[vertex.key]

        for i in self.dict.keys():
            if self.dict[i] > pom:
                self.dict[i] -=1

    def deleteEdge(self, vertex1, vertex2):

        for i in range(len(self.edge) - 1, -1, -1):
            if vertex1 == self.edge[i][0] and vertex2 == self.edge[i][1]:
                del self.edge[i]

        self.matrix[self.dict[vertex1.key]][self.dict[vertex2.key]] = 0

    def getVertexIdx(self, vertex):

        if vertex in self.vertex:
            return  self.dict[vertex.key]
        else:
            return None

    def getVertex(self, vertex_idx):

        if vertex_idx < len(self.edge) and vertex_idx >= 0:
            for key, ind in self.dict.items():
                if ind == vertex_idx:
                    print(key)
        else:
            return None

    def neighbours(self, vertex_idx):
        pom = []

        if vertex_idx not in self.dict.values():
            return None

        else:
            pom2=0
            for i in self.matrix[vertex_idx]:
                if i == 1:
                    pom.append(pom2)
                pom2+=1
            return pom

    def order(self):
        return len(self.vertex)

    def size(self):
        return len(self.edge)

    def edges(self):

        edge = []

        for i in self.edge:
            pom = (i[0].key, i[1].key)
            edge.append(pom)
        return edge

class List:

    def __init__(self):
        self.vertex = []
        self.edge = []
        self.list = {}
        self.dict = {}

    def insertVertex(self, vertex):

        self.vertex.append(vertex)
        self.dict[vertex.key] = len(self.list)

        self.list[len(self.list)] = []

    def insertEdge(self, vertex1, vertex2, egde=1):

        self.edge.append([vertex1, vertex2])

        self.list[self.dict[vertex1.key]].append(self.dict[vertex2.key])

    def deleteVertex(self, vertex):

        pom = self.dict[vertex.key]

        self.vertex.remove(vertex)

        for i in range(len(self.edge) - 1, -1, -1):
            if vertex in self.edge[i]:
                del self.edge[i]

        if pom == len(self.list)-1:
            del self.list[pom]
        else:
            for i in range(len(self.list)):
                if i > pom:
                    pom2 = self.list[i]
                    self.list[i - 1] = pom2
                    del self.list[i]


        for i in range(len(self.list)):
            for j in range(len(self.list[i]) - 1, -1, -1):
                if self.list[i][j] == pom:
                    self.list[i].remove(pom)
                elif self.list[i][j] > pom:
                    self.list[i][j] -= 1

        #slownik
        del self.dict[vertex.key]

        for i in self.dict.keys():
            if self.dict[i] > pom:
                self.dict[i] -= 1

    def deleteEdge(self, vertex1, vertex2):

        for i in range(len(self.edge) - 1, -1, -1):
            if vertex1 == self.edge[i][0] and vertex2 == self.edge[i][1]:
                del self.edge[i]

        self.list[self.dict[vertex1.key]].remove(self.dict[vertex2.key])

    def getVertexIdx(self, vertex):

        if vertex in self.vertex:
            return self.dict[vertex.key]
        else:
            return None

    def getVertex(self, vertex_idx):

        if vertex_idx < len(self.edge) and vertex_idx >= 0:
            for key, ind in self.dict.items():
                if ind == vertex_idx:
                    print(key)
        else:
            return None

    def neighbours(self, vertex_idx):
        return self.list[self.dict[vertex_idx.key]]

    def order(self):
        return len(self.vertex)

    def size(self):
        return len(self.edge)

    def edges(self):
        edge = []

        for i in self.edge:
            pom = (i[0].key, i[1].key)
            edge.append(pom)
        return edge

def main():
    lst = List()
    mat = Matrix()

    for i in range(len(polska.polska)):
        mat.insertVertex(Vertex(polska.polska[i][2], polska.polska[i][0], polska.polska[i][1]))
        lst.insertVertex(Vertex(polska.polska[i][2], polska.polska[i][0], polska.polska[i][1]))

    for i in range(len(polska.graf)):
        for j in lst.vertex:
            if polska.graf[i][0] == j.key:
                pom1 = j
            if polska.graf[i][1] == j.key:
                pom2 = j

        lst.insertEdge(pom1, pom2)
        mat.insertEdge(pom1, pom2)

    for i in lst.vertex:
        if i.key == 'K':
            pom1 = i
        if i.key == 'E':
            pom2 = i
        if i.key == "W":
            pom3 = i
    lst.deleteVertex(pom1)
    mat.deleteVertex(pom1)
    lst.deleteEdge(pom2, pom3)
    lst.deleteEdge(pom3, pom2)
    mat.deleteEdge(pom2, pom3)
    mat.deleteEdge(pom3, pom2)


    polska.draw_map(lst.edges())
    polska.draw_map(mat.edges())


if __name__ == '__main__':
    main()