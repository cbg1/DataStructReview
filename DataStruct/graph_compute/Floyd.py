# coding:utf-8
from DataStruct.graph_compute.ljjz import *

'''
Floyd
所有顶点对的最短路径
'''
def floyd(g, p, d):

    for i in range(g.n):
        for j in range(g.n):
            d[i][j] = g.edges[i][j]
            if (i != j and d[i][j] < FINITY):
                p[i][j] = i
            else:
                p[i][j] = -1
    for k in range(g.n):
        for i in range(g.n):
            for j in range(g.n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = k


if __name__ == '__main__':
    vexs = [0] * M
    edges = [[0] * M for i in range(M)]
    n = 0
    e = 0
    g = Mgraph(vexs, edges, n, e)
    create(g, "floyd.txt", 1)
    d = [[FINITY] * M for i in range(M)]
    p = [[None] * M for i in range(M)]
    floyd(g, p, d)
    print("d:", d)
    print("p:", p)
