# coding:utf-8
from DataStruct.graph_compute.ljjz import *


class edge:
    def __init__(self, beg, en, length):
        self.beg = beg
        self.en = en
        self.length = length


def prim(g, tree):
    # tree是用来存放最小生成树的集合
    for v in range(1, g.n):  # 初始化树边集,从第一个顶点开始
        edgedata = edge(0, v, g.edges[0][v])
        tree[v - 1] = edgedata
    for t in tree:
        print(t.beg, t.en, t.length)
    for k in range(g.n - 2):  # 依次求最小边加入tree
        # tree中的第一条边作为最小，依次中找出最小边
        min = tree[k].length
        s = k
        for j in range(k + 1, g.n - 1):
            if (tree[j].length < min):
                min = tree[j].length
                s = j
        # 顺着边的en节点往下找，找到的那条边与初始进行替换
        v = tree[s].en
        x = tree[s]
        tree[s] = tree[k]
        tree[k] = x
        # 以当前两栖边的终止节点作为起点往下寻找并加入tree集合
        for j in range(k + 1, g.n - 1):
            d = g.edges[v][tree[j].en]
            if d < tree[j].length:
                tree[j].length = d
                tree[j].beg = v
        for t in tree:
            print(t.beg, t.en, t.length)

    print("输出最小生成树:")
    for j in range(g.n - 1):
        print(g.vexs[tree[j].beg], " --- ", g.vexs[tree[j].en], " ", tree[j].length)


if __name__ == '__main__':
    vexs = [0] * M
    edges = [[0] * M for i in range(M)]
    n = 0
    e = 0
    g = Mgraph(vexs, edges, n, e)
    filename = "prim.txt"
    c = 0
    # 创建无向连接图
    create(g, filename, c)
    edgedata = edge(None, None, None)
    tree = [edgedata] * (M - 1)
    prim(g, tree)
