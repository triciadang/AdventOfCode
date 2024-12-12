import collections

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited = [False] * (max(self.graph))+1

        queue = []

        queue.append(s)
        visited[s] = True
        
        while queue:
            s=queue.pop(0)

            print(s,end=" ")

            for i in self.graph[s]:
                if i not in visited[i]:
                    queue.append(i)
                    visited[i] = True

def main():
    with open("input.txt") as f:
        n = int(f.readline().strip())
        lines = [f.readline().strip() for _ in range(n)]

    number_of_lines = len(lines)
    number_of_indices = len(lines[0])

    list_of_zeroes = []
    list_of_nines = []

    for i in range(0,number_of_lines):
        for j in range(0,number_of_indices):

            str_i = str(i)
            str_j = str(j)
            node1 = f"{lines[i][j]}-{str_i}-{str_j}"
            current_value_int = int(lines[i][j])


            if lines[i][j] == '0':
                list_of_zeroes.append(f"{node1}")
            if lines[i][j] == '9':
                list_of_nines.append(f"{node1}")

            #check above
            if i-1 >= 0:
                if int(lines[i-1][j]) == current_value_int+1:
                    str_i = str(i-1)
                    str_j = str(j)
                    node2 = f"{lines[i-1][j]}-{str_i}-{str_j}"
                    g.add_edge(node1,node2)
                    print(node1,node2)

            #check below
            if i+1 < number_of_lines:
                if int(lines[i+1][j]) == current_value_int+1:
                    str_i = str(i+1)
                    str_j = str(j)
                    node2 = f"{lines[i+1][j]}-{str_i}-{str_j}"
                    g.add_edge(node1,node2)
                    print(node1,node2)

            #check left
            if j-1 >= 0:
                if int(lines[i][j-1]) == current_value_int+1:
                    str_i = str(i)
                    str_j = str(j-1)
                    node2 = f"{lines[i][j-1]}-{str_i}-{str_j}"
                    g.add_edge(node1,node2)
                    print(node1,node2)

            #check right
            if j+1 < number_of_indices:
                if int(lines[i][j+1]) == current_value_int+1:
                    str_i = str(i)
                    str_j = str(j+1)
                    node2 = f"{lines[i][j+1]}-{str_i}-{str_j}"
                    g.add_edge(node1,node2)
                    print(node1,node2)


    visited = [[False] * n for _ in range(n)]

    max_area = 0
    min_perimeter = float("inf")

    for i in range(n):
        for j in range(n):
            if lines[i][j] != "A" or visited[i][j]:
                continue

            area,perimeter = g.BFS(lines)

            if area > max_area or (area == max_area and perimeter < min_perimeter):
                max_area = area
                min_perimeter = perimeter

                
if __name__ == '__main__':
    main()