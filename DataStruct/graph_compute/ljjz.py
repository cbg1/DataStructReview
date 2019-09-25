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


if __name__ == '__main__':
    vexs = [0] * M
    edges = [[0] * M for i in range(M)]
    n = 0
    e = 0
    g = Mgraph(vexs, edges, n, e)
    s = "s.txt"
    c = 0
    create(g, s, c)
