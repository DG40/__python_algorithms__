graph = {}
graph['a'] = {'b':5, 'c':2} # - start
graph['b'] = {'d':4, 'e':2}
graph['c'] = {'b':8, 'e':7}
graph['d'] = {'e':6, 'f':3}
graph['e'] = {'f':1}
graph['f'] = {} # - end

costs = {'a':0, 'b':float('inf'), 'c':float('inf'), 'd':float('inf'), 'e':float('inf'), 'f':float('inf')}
parents = {'a':None, 'b':None, 'c':None, 'd':None, 'e':None, 'f':None}
processed = set()


def find_smallest_node():
    lowest_cost = float('inf')
    lowest_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_node = node
    return lowest_node


def form_road(node, chain):
    chain.append(node)
    if parents[node] == None:
        return
    else:
        form_road(parents[node], chain)
    

node = find_smallest_node()
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_smallest_node()
    
print(costs)
print(parents)

road = []
form_road('f', road)
print(road[::-1])
