# coding:utf-8
from DataStruct.graph_compute.ljjz import *


class edge:
    def __init__(self, beg, en, length):
        self.beg = beg
        self.en = en
        self.length = length


def quick_sort(edges, left, right):
    if left < right:
        i = left
        j = right
        x = edges[i]
        while i < j:
            while i < j and edges[j].length >= x.length:
                j -= 1
            edges[i] = edges[j]
            while i < j and edges[i].length < x.length:
                i += 1
            edges[j] = edges[i]
        edges[i] = x
        # 递归实现
        quick_sort(edges, left, i - 1)
        quick_sort(edges, i + 1, right)


def get_edge(g, edges):
    k = 0
    for i in range(g.n):
        for j in range(i):
            if (g.edges[i][j] != 0 and g.edges[i][j] < FINITY):
                # print(i, j, g.edges[i][j])
                edgedata = edge(i, j, g.edges[i][j])
                edges[k] = edgedata
                k = k + 1


def kruskal(g):
    edgedata = edge(None, None, None)
    cnvx = [None] * M
    k = 0
    edges = [edgedata] * (M * M)  # 存放图所有边
    tree = [edgedata] * M  # 存放最小生成树
    get_edge(g, edges)  # 读取所有边
    # print("排序前")
    # for e in edges:
    #     print("tets:", e.beg, e.en, e.length)
    quick_sort(edges, 0, g.e - 1)  # 对边升序
    # print("排序后")
    # for e in edges:
    #     print("tets:", e.beg, e.en, e.length)
    # 对顶点编号,每个点为单个连通分量
    for i in range(g.n):
        cnvx[i] = i
    # n个顶点要n-1条边连接
    for i in range(g.n - 1):
        while (cnvx[edges[k].beg] == cnvx[edges[k].en]):
            k += 1
        tree[i] = edges[k]
        ltfl = cnvx[edges[k].en]  # 选中边的终点
        for j in range(g.n):  # 两个连通分量合并为一个,下次用的时候该点变了，最终所有连通变量都为同一个
            if cnvx[j] == ltfl:
                cnvx[j] = cnvx[edges[k].beg]
        k += 1
    print("最小生成树为：")
    for j in range(g.n - 1):
        print(g.vexs[tree[j].beg], "---", g.vexs[tree[j].en], " ", tree[j].length)


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
    kruskal(g)
