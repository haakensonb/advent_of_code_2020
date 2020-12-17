import re

def build_graph_from_input(input_file_path):
    graph = {}
    with open(input_file_path) as f:
        for line in f.readlines():
            # Remove ending period and trailing space.
            line = line.replace(".", "").strip()
            # Split line into seperate rules based on multiple delimiters.
            line = re.split(r'\scontain\s|, ', line)
            node = line[0].strip().split(" bag")[0]
            # Create adjacency list for each node
            graph[node] = []
            for rule in line[1:]:
                # Ignore empty case of 'no other bags'
                if not rule.startswith("no other"):
                    split_rule = re.split(r'(\d+)| bag', rule)
                    # Extract edge weight and child node name.
                    weight = split_rule[1]
                    name = split_rule[2].strip()
                    # Edges are tuples of form (child_key, edge_weight)
                    edge = (name, int(weight))
                    if edge not in graph[node]:
                        graph[node].append(edge)
            # print(f"node: {node}, edges:{graph[node]}")
    return graph


def has_path(graph, current, destination):
    # If current node is a dead end.
    if not graph[current]:
        return False
    
    if current == destination:
        return True

    # The more concise way to rewrite the code below.
    # return any([has_path(graph, child[0], destination) for child in graph[current]])

    # Check to see if any paths are valid.
    paths = []
    for edge in graph[current]:
        child = edge[0]
        paths.append(has_path(graph, child, destination))
    for path in paths:
        if path:
            return True
    return False


def get_path_weight(graph, current):
    # Base case: no adjacent nodes
    if not graph[current]:
        return 0
    
    total = 0

    # For each child node
    for edge in graph[current]:
        child = edge[0]
        weight = edge[1]
        # Recursively call until reaching a base case with a value.
        # Result is the number of bags contained within a bag.
        # Weight is the multiplier value found using edge weight.
        result = get_path_weight(graph, child)
        # After results are found, total them up.
        total += (weight + (weight * result))
    
    return total

if __name__ == "__main__":
    print("Part 1:")
    graph = build_graph_from_input("input.txt")
    destination_node = "shiny gold"
    possible_nodes = [key for key in graph.keys() if key != destination_node]
    print(sum([has_path(graph, node, destination_node) for node in possible_nodes]))
    print("Part 2:")
    print(get_path_weight(graph, destination_node))

