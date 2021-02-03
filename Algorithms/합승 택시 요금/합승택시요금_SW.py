import heapq

def solution(n, s, a, b, fares):
    arr = [[] for _ in range(n+1)]
    
    for c, d, f in fares:
        arr[c].append((f,d))
        arr[d].append((f,c))
    
    def dijkstra(start,end):
        heap = [(0,start)]
        fare_map = [1e9 for _ in range(n+1)]
        
        while heap:
            start_fare, start_idx, = heapq.heappop(heap)
            fare_map[start_idx] = start_fare
            
            # 목적지라면
            if start_idx == end:
                return start_fare
            
            for dst_fare, dst_idx in arr[start_idx]:
                # 방문하지 않았다면
                if fare_map[dst_idx] == 1e9:
                    heapq.heappush(heap,(start_fare+dst_fare,dst_idx))
        
        return 1e9    
    
    answer = 1e9
    
    for i in range(1,n+1):
        answer= min(answer,(dijkstra(a,i) + dijkstra(b,i) + dijkstra(s,i)))
    
    return answer