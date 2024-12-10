from collections import defaultdict
import networkx as nx

def main():

    with open("input.txt") as f:
        lines = f.readlines()

    g = nx.DiGraph()

    print(len(lines))
    number_of_lines = len(lines)
    number_of_indices = len(lines[0])-1

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

    print(list_of_zeroes)
    print(list_of_nines)
    

    score = set()
    ratings = 0

    for each_zero in list_of_zeroes:
        for each_nine in list_of_nines:
            if g.has_node(each_zero) and g.has_node(each_nine):

                if nx.has_path(g,each_zero,each_nine):
                    score.add((each_zero,each_nine))
                    paths = nx.all_simple_paths(g,source=each_zero,target=each_nine)
                    for each_path in paths:
                        ratings += 1

                

    print(len(score))
    print(ratings)


if __name__ == '__main__':
    main()