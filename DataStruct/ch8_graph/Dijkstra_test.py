# coding:utf-8
from DataStruct.graph_compute.ljjz import *

'''
Dijkstra
先选出距离v0最短的点，
然后，利用这个最短的点作为中间节点改写其他节点，依次，选出所有可选的点即可完成
'''


# 单源点到其他个点的最短路径
def dijkstra(g, v0, p, d):
    v = 0
    # 表示当前元素是否已经求出最短路径
    final = [False] * M
    # 初始化S与距离向量d
    for v in range(g.n):
        final[v] = False
        d[v] = g.edges[v0][v]
        if (d[v] < FINITY and d[v] != 0):  # v0和该点之间有连接，否则为-1且排除v0
            p[v] = v0
        else:
            p[v] = -1
    # final 是集合，d为v0与各点距离，p为v0与各点有路径
    # 初始化的集合s只有一个节点v0
    final[v0] = True
    d[v0] = 0
    print(d)
    # 处理v-s中的其他顶点
    for i in range(1, g.n):
        min = FINITY
        for k in range(g.n):
            # 找到与v0距离最近的顶点v
            if (not final[k] and d[k] < min):  # 从v-s中找最小的边节点
                v = k
                min = d[k]
        print(g.vexs[v], "---", min)
        if min == FINITY:
            return
        final[v] = True
        # 对前面选出了的点修改距离，找中间点取待直连
        for k in range(g.n):
            if (not final[k] and (min + g.edges[v][k] < d[k])):
                d[k] = min + g.edges[v][k]
                p[k] = v


# 打印距离产生的路径,先进后出原则最终目标点先入栈，再寻找中间结果依次入栈
def print_gpd(g, p, d):
    print("p:", p)
    print("d:", d)
    # 定义空栈并初始化
    st = [None] * M
    # pre = -1
    top = -1
    for i in range(g.n):
        print("point:", i, " Distanced:", d[i])
        top += 1
        st[top] = i
        pre = p[i]
        while pre != -1:
            top += 1
            st[top] = pre
            pre = p[pre]
        while top > 0:
            print("->", st[top], end="")
            top -= 1
        print(" st:", st)
        print()


if __name__ == '__main__':
    vexs = [0] * M
    edges = [[0] * M for i in range(M)]
    n = 0
    e = 0
    g = Mgraph(vexs, edges, n, e)
    create(g, "dijkstra.txt", 1)
    print("please input source point v0:")
    v0 = int(input())
    d = [FINITY] * M
    p = [None] * M
    dijkstra(g, v0, p, d)
    print("打印路径:")
    print_gpd(g, p, d)
