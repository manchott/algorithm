def solution(n, paths, gates, summits):
    def DFS(x, intensity):
        if x in summits:
            answer.append([x, intensity])
            return
        if intensity > max_intensity :
            return
        for i in range(1, n + 1):
            if grid[x][i] and not visited[i]:
                if i in gates:
                    continue
                visited[i] = 1
                DFS(i, max(intensity, grid[x][i]))
                visited[i] = 0

    answer = []
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    max_intensity = float('inf')
    visited = [0] * (n + 1)
    for s, e, num in paths:
        grid[s][e] = num
        grid[e][s] = num
    for gate in gates:
        visited[gate] = 1
        DFS(gate, 0)
        visited[gate] = 0

    answer.sort(key=lambda x:(x[1], x[0]))
    return answer[0]
inpt = 7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]
print(solution(*inpt))
