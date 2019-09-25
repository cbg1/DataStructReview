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


# 邻接表图
class LinkedGraph:
    def __init__(self, adjlist, n, e):
        self.adjlist = adjlist  # list存放头结点的顺序表
        self.n = n  # 图的顶点数
        self.e = e  # 图的边数


# 构建图
def create():
    vertex_list = [0, 1, 2, 3, 4, 5]
    edge_lists = [[1, 2], [0, 3, 4], [0, 5], [1, 4], [1, 3, 5], [2, 4]]
    vertexnode = VertexNode(0, None)
    g = LinkedGraph([vertexnode] * len(vertex_list), len(vertex_list), sum(len(i) for i in edge_lists))  # 构建的为无向图则除以2
    for vex, edge_list in zip(vertex_list, edge_lists):
        vertexnode = VertexNode(vex, None)
        g.adjlist[vex] = vertexnode
        # 头节点中加入边节点
        next = None
        for edge in edge_list[::-1]:
            current = EdgeNode(edge, next)
            next = current
        g.adjlist[vex].firstEdge = next
    return g


# 从i点开始深度遍历
def dfs(g, i, visited):
    print("visit vertex:", g.adjlist[i].vertex)
    visited[i] = 1
    p = g.adjlist[i].firstEdge
    while p:
        if not visited[p.adjvex]:
            dfs(g, p.adjvex, visited)
        p = p.next


def DfsTraverse(g, visited):
    for i in range(g.n):
        if not visited[i]:
            dfs(g, i, visited)


if __name__ == '__main__':
    g = create()
    # 查看图的创建情况
    # for i in range(g.n):
    #     print()
    #     print("头结点: ", g.adjlist[i].vertex)
    #     edge = g.adjlist[i].firstEdge
    #     print("边节点:", end="")
    #     while edge:
    #         print(edge.adjvex, end=" ")
    #         edge = edge.next
    #     print("\n+++++++++++++++++++++++++++++++++++++++", end="")
    # 初始化标志
    visited = [0] * M
    DfsTraverse(g, visited)
