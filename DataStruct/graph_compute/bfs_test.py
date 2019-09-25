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
def bfs(g, i, visited):
    # 初始化队列
    queue = [0] * M
    front = 0
    rear = 0
    print("源点:", g.adjlist[i].vertex)
    visited[i] = 1
    queue[rear] = i
    rear += 1
    while rear > front:  # 队列为非空时候执行循环体
        j = queue[front]
        front += 1
        p = g.adjlist[j].firstEdge
        while p:
            # 广度优先遍历邻接表
            if visited[p.adjvex] == 0:
                print("访问中间节点:", g.adjlist[p.adjvex].vertex)
                queue[rear] = p.adjvex
                rear += 1
                visited[p.adjvex] = 1
            print(queue)
            p = p.next


def BfsTraverse(g, visited):
    count = 0  # 连通分量的个数
    for i in range(g.n):
        if not visited[i]:
            count += 1
            bfs(g, i, visited)
    return count


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
    count = BfsTraverse(g, visited)
    print("该图共有几个连通分量:", count)
