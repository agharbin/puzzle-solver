#
# Solver.py
# 
# A simple DFS backtracking solver for finding a Hamiltonian path through the graph defined by "edges.txt"
#

def load_edges(filename):
    infile = open(filename,"r")
    start_edge = infile.readline().strip()
    goal_edge = infile.readline().strip()
    edges = {}
    for line in infile:
        line = line.strip().split()
        edges[line[0]] = (line[1],line[2],line[3],line[4])
    return (start_edge,goal_edge,edges)

def all_visited(visited):
    for edge,status in visited.iteritems():
        if status == False:
            return False
    return True

def print_stack(stack):
    print " ".join([i[0] for i in stack]) 

if __name__ == "__main__":
    S,G,E = load_edges("edges.txt")
    stack = []
    visited = {key: False for key in E.keys()}

    # Add starting node to the queue
    stack.append((S,-1))
    visited[S] = True

    print "Searching..."
    while True:
        # Check failure condition
        if len(stack) == 0:
            print "No solution found"
            break
        # Check success condition
        if stack[-1][0] == G and all_visited(visited):
            print "Success:"
            print_stack(stack)
            break
        # Pop top node from stack and advance to its next child
        curr = stack.pop()
        visited[curr[0]] = False
        curr = (curr[0], curr[1] + 1)
        if curr[1] >= 4:
            # The current node is exhausted, so let it fall off the stack without re-pushing it
            continue 
        next_v = E[curr[0]][curr[1]]
        if next_v != "--" and visited[next_v] == False:
            # push the current vertex back on the stack and explore its next child
            stack.append(curr)
            visited[curr[0]] = True
            stack.append((next_v,-1))
            visited[next_v] = True
        else:
            # keep this vertex on top to try if its next child can be explored
            stack.append(curr) 
            visited[curr[0]] = True
