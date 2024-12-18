DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Graph:
   def __init__(self, graph: dict = {}):
       self.graph = graph  # A dictionary for the adjacency list

   def add_edge(self, node1, node2, weight):
       if node1 not in self.graph:  # Check if the node is already added
           self.graph[node1] = {}  # If not, create the node
       self.graph[node1][node2] = weight  # Else, add a connection to its neighbor


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    map = []

    for i in range(lines):
        map.append(list(lines[i].strip()))

    for i in range(0,number_of_lines):
        for j in range(0,number_of_indices):

            str_i = str(i)
            str_j = str(j)

            if lines[i][j] == ".":
                node1 = f"{lines[i][j]}-{str_i}-{str_j}"

                for dx, dy in DIRECTIONS:
                    






    

if __name__ == '__main__':
    main()