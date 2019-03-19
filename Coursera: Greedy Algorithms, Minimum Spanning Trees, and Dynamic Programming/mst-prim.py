import re
from collections import defaultdict
from heapq import *


def getGraph(fPath="edges.txt"):
    '''
    edges.txt format:

    numVertices,numEdges
    node1,node2,weight
    node1,node3,weight...

    eg:
    500,2704
    1,2,-30
    2,5,4
    ...
    '''
    file = open('edges.txt', 'r')
    p = re.compile('-?\d+')

    numVertices, numEdges = map(int, p.findall(file.readline()))
    print(numVertices, numEdges)

    adjacent_vertex = defaultdict(list)
    for i in range(numEdges):
        v1, v2, weight = map(int, p.findall(file.readline()))
        adjacent_vertex[v1].append((weight, v1, v2))
        adjacent_vertex[v2].append((weight, v2, v1))

    file.close()
    return adjacent_vertex, numVertices


def mstPrim(adjacent_vertex, numVertices, r=1):
    '''
    :adjacent_vertex: dict,index为[节点1],value为(边权重,节点1,节点2)
    :numVertices: 节点总数
    :r: 初始节点
    '''
    mst = []  # 记录返回最小生成树
    X = {r}  # 记录加入的节点
    q = adjacent_vertex[r]  # 节点的邻接表表示
    heapify(q)

    while len(X) != numVertices:
        w, v1, v2 = heappop(q)
        if v2 not in X:
            X.add(v2)
            mst.append([v1, v2, w])
            for v in adjacent_vertex[v2]:
                if v[2] not in X:
                    heappush(q, v)

    return mst
