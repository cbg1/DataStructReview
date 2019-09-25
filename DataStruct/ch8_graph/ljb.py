# coding:utf-8
# 邻接表
M = 20


# 边节点
class EdgeNode:
    def __init__(self, adjvex, next):
        self.adjvex = adjvex
        self.next = next


# 头结点
class VertexNode:
    def __init__(self, vertex, firstEdge):
        self.vertex = vertex
        self.firstEdge = firstEdge


class LinkedGraph:
    def __init__(self, adjlist, n, e):
        self.adjlist = adjlist
        self.n = n
        self.e = e


def create(g, filename, c):
    f = open(filename, "r")  # 设置文件对象
    if f is not None:
        lines = f.readlines()
        g.n, g.e = int(lines[0].strip("\n").split(" ")[0]), int(lines[0].strip("\n").split(" ")[1])
        # 顶点信息，边节点置为空
        for index, vex in enumerate(list(lines[1].strip("\n"))):
            g.adjlist[index].vertex = int(vex)
            g.adjlist[index].firstEdge = None

        for k in range(g.e):
            i = int(lines[k + 2].strip("\n").split(" ")[0])
            j = int(lines[k + 2].strip("\n").split(" ")[1])
            w = int(lines[k + 2].strip("\n").split(" ")[2])

            s = EdgeNode(j, adjlist[i].firstEdge)
            g.adjlist[i].firstEdge = s
            if c == 0:
                s = EdgeNode(i, g.adjlist[j].firstEdge)
                g.adjlist[j].firstEdge = s

        f.close()
    else:
        g.n = 0

    for i in range(g.n):
        print(g.adjlist[i].vertex)


if __name__ == '__main__':
    adjlist = []
    for i in range(M):
        vertex = VertexNode(None, None)
        adjlist.append(vertex)
    n = 0
    e = 0
    g = LinkedGraph(adjlist, n, e)
    filename = "s.txt"
    c = 0
    create(g, filename, c)
