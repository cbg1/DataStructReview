# coding:utf-8
# 邻接矩阵

FINITY = 5000
M = 20


class Mgraph:
    def __init__(self, vexs, edges, n, e):
        self.vexs = vexs
        self.edges = edges
        self.n = n
        self.e = e


def create(g, s, c):
    f = open(s, "r")  # 设置文件对象
    if f is not None:
        lines = f.readlines()
        g.n, g.e = int(lines[0].strip("\n").split(" ")[0]), int(lines[0].strip("\n").split(" ")[1])
        for index, vex in enumerate(list(lines[1].strip("\n"))):
            g.vexs[index] = int(vex)
        for i in range(g.n):
            for j in range(g.n):
                if i == j:
                    g.edges[i][j] = 0
                else:
                    g.edges[i][j] = FINITY
        for k in range(g.e):
            i = int(lines[k + 2].strip("\n").split(" ")[0])
            j = int(lines[k + 2].strip("\n").split(" ")[1])
            w = int(lines[k + 2].strip("\n").split(" ")[2])
            g.edges[i][j] = w
            if c == 0:  # 建立无向连接图
                g.edges[j][i] = w
        f.close()  # 关闭文件
    else:
        g.n = 0
    print(g.vexs)
    print(g.edges)


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
