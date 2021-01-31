import heapq

def dijkstra(n, graph, start):
    q = []
    distance = [1e9 for _ in range(n+1)]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[1:]

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for node1, node2, cost in fares:
        graph[node1].append([node2, cost])
        graph[node2].append([node1, cost])
    
    s_distance = dijkstra(n, graph, s)
    a_distance = dijkstra(n, graph, a)
    b_distance = dijkstra(n, graph, b)
    
    answer = 1e9
    for s_fare, a_fare, b_fare in zip(s_distance, a_distance, b_distance):
        fare = sum([s_fare, a_fare, b_fare])
        if answer > fare: answer = fare
    return answer