# coding:utf-8
'''拓扑排序'''
# AOV网邻接表存储
M = 20


class edgenode:  # 边界点
    def __init__(self, adjvex, next):
        self.adjvex = adjvex
        self.next = next


class vertextnode:  # 带顶点入度的头结点
    def __init__(self, firstedge, vertetx, id):
        self.vertex = vertetx
        self.firstedge = firstedge
        self.id = id  # 入度


class AovGraph:  # AOV网邻接表结构
    def __init__(self, adjlist, n, e):
        self.adjlist = adjlist
        self.n = n
        self.e = e


# 构建图
def create():
    vertex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    id_list = [0, 0, 2, 2, 1, 2, 2, 1, 1]
    edge_lists = [[2, 7], [2, 4], [3], [5, 6], [3, 5], [], [], [8], [6]]
    vertexnode = vertextnode(None, None, None)
    g = AovGraph([vertexnode] * len(vertex_list), len(vertex_list), sum(len(i) for i in edge_lists))  # 构建的为无向图则除以2
    for vex, edge_list, id in zip(vertex_list, edge_lists, id_list):
        # print(vex, edge_list, id)
        vertexnode = vertextnode(None, vex, id)
        g.adjlist[vex] = vertexnode
        # 头节点中加入边节点
        next = None
        for edge in edge_list[::-1]:
            current = edgenode(edge, next)
            next = current
        g.adjlist[vex].firstedge = next
    return g


def top_sort(g):
    k = 0
    # 队列
    queue = [None] * M
    front = 0
    rear = 0
    flag = [0] * g.n
    # 入度为0的节点入队
    for i in range(g.n):
        if g.adjlist[i].id == 0 and flag[i] == 0:
            queue[rear] = i
            rear += 1
            flag[i] = 1
    print("AOV网的拓扑序列是：")
    # 当队列不为空时，队首元素出队
    while front < rear:
        v = queue[front]
        front += 1
        print(g.adjlist[v].vertex, end="->")
        # 计数器加一
        k += 1
        p = g.adjlist[v].firstedge
        # print(p)
        while p:
            j = p.adjvex
            g.adjlist[j].id = g.adjlist[j].id - 1
            if (g.adjlist[j].id == 0 and flag[j] == 0):
                queue[rear] = j
                rear += 1
                flag[j] = 1
            p = p.next
    return k


if __name__ == '__main__':
    vertex = vertextnode(None, None, None)
    adjlist = [vertex] * M
    g = create()
    # # 查看邻接表
    # for i in range(g.n):
    #     vex = g.adjlist[i].vertex
    #     id = g.adjlist[i].id
    #     print(vex, id)
    #     p = g.adjlist[vex].firstedge
    #     while p:
    #         print(p.adjvex, end="->")
    #         p = p.next
    #     print()
    top_sort(g)
