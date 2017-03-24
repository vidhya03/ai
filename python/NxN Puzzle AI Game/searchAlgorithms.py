from state import *
from collections import deque

def updateMaxFringe(frontier, max_fringe_size):
    if(len(frontier) > max_fringe_size):
        max_fringe_size = len(frontier)

    return max_fringe_size

def updateMaxDepth(node, max_search_depth):
    if(node.depth > max_search_depth):
        max_search_depth = node.depth

    return max_search_depth



def bfs(start):
    lst = start.split(',')
    lst = list(map(int, lst))

    beginningBoard = tuple(lst)
    initialize(lst)

    neighborsList = []
    frontier = deque()
    frontier.append(create_node(beginningBoard, None, None, 0, 0 ))
    max_fringe_size = 1
    max_search_depth = 0
    nodes_expanded = 0
    explored = set()

    while frontier:
        node = frontier.popleft()

        if(node.state in explored):
            continue
        
        explored.add(node.state)

        if(goalTest(node)):
            lst = []
            lst.append(node)
            lst.append(max_fringe_size)
            lst.append(len(frontier))
            lst.append(max_search_depth)
            lst.append(nodes_expanded)
            return lst  

        nodes_expanded = nodes_expanded+1

        neighborsList = expand_nodes(node)
        for neighbor in neighborsList:
            if(neighbor.state in explored):
                continue
            elif(neighbor not in frontier):
                frontier.append(neighbor)
                max_fringe_size = updateMaxFringe(frontier, max_fringe_size)
                max_search_depth = updateMaxDepth(neighbor, max_search_depth)
    return False


            
def dfs(start):
    lst = start.split(',')
    lst = list(map(int, lst))

    beginningBoard = tuple(lst)
    
    # initiate variables
    initialize(lst)
     
    firstNode = create_node(beginningBoard,None,None,0,0)
    frontier = deque()
    frontier.append(firstNode)
    explored = set()

    nodes_expanded = 0
    fringe_size = len(frontier)
    max_fringe_size = fringe_size
    max_search_depth = 0
    running_time = 0
    
    # main search loop
    while frontier:
        node = frontier.pop()   
        explored.add(node.state) 

  
        if(goalTest(node)):
            lst = []
            lst.append(node)
            lst.append(max_fringe_size)
            lst.append(len(frontier))
            lst.append(max_search_depth)
            lst.append(nodes_expanded)
            return lst   

        nodes_expanded = nodes_expanded+1

        # expand current node
        neighborsList = expand_nodes_reverse(node)
        for neighbor in neighborsList:
            if neighbor.state not in explored:
                frontier.append(neighbor)
                explored.add(neighbor.state)
                max_fringe_size = updateMaxFringe(frontier, max_fringe_size)
                max_search_depth = updateMaxDepth(neighbor, max_search_depth)

    return False        
 


def ast(start):
    lst = start.split(',')
    lst = list(map(int, lst))

    beginningBoard = tuple(lst)
    initialize(lst)

    neighborsList = []
    frontier = []
    cost = manhattanCostFunction(beginningBoard)
    heappush(frontier, create_node(beginningBoard, None, None, 0, cost ))
    
    max_fringe_size = 1
    max_search_depth = 0
    nodes_expanded = 0
    explored = set()

    while frontier:
        node = heappop(frontier)
        print("Parent: ", node.state, node.direction)
        
        if(node.state in explored):
            continue
        
        explored.add(node.state)

        if(goalTest(node)):
            lst = []
            lst.append(node)
            lst.append(max_fringe_size)
            lst.append(len(frontier))
            lst.append(max_search_depth)
            lst.append(nodes_expanded)
            return lst  
        
        nodes_expanded = nodes_expanded+1

        neighborsList = expand_nodes_ast(node)
        for neighbor in neighborsList:
            if(neighbor.state in explored):
                continue
            elif(neighbor not in frontier):
                print(neighbor.state, neighbor.direction)
                heappush(frontier, neighbor)
                max_fringe_size = updateMaxFringe(frontier, max_fringe_size)
                max_search_depth = updateMaxDepth(neighbor, max_search_depth)
            
    return False




def ast_limit(beginningBoard, cost_limit, nodes_expanded, max_fringe_size, max_search_depth):

    neighborsList = []
    frontier = []
    cost = manhattanCostFunction(beginningBoard)
    heappush(frontier, create_node(beginningBoard, None, None, 0, cost ))
    explored = set()

    while frontier:
        node = heappop(frontier)
        print("Parent: ", node.state, node.direction)
        
        if(node.state in explored):
            continue
        
        explored.add(node.state)

        if(goalTest(node)):
            lst = []
            lst.append(node)
            lst.append(max_fringe_size)
            lst.append(len(frontier))
            lst.append(max_search_depth)
            lst.append(nodes_expanded)
            return lst  
        
        nodes_expanded = nodes_expanded+1

        neighborsList = expand_nodes_ast(node)
        for neighbor in neighborsList:
            if(neighbor.cost > cost_limit):
		continue
            elif(neighbor.state in explored):
                continue
            elif(neighbor not in frontier):
                print(neighbor.state, neighbor.direction)
                heappush(frontier, neighbor)
                max_fringe_size = updateMaxFringe(frontier, max_fringe_size)
                max_search_depth = updateMaxDepth(neighbor, max_search_depth)
            
    return None

def ida(start):
    lst = start.split(',')
    lst = list(map(int, lst))

    beginningBoard = tuple(lst)
    initialize(lst)

    cost_limit =1 
    nodes_expanded = 0 
    max_fringe_size = 1
    max_search_depth = 0
    running_time = 0
    
    # main search loop
    while(1):

        if(ast_limit(beginningBoard, cost_limit, nodes_expanded, max_fringe_size, max_search_depth)==None):
            cost_limit += 1
            ast_limit(beginningBoard, cost_limit, nodes_expanded, max_fringe_size, max_search_depth)
        else:
            lst = []
            lst =  ast_limit(beginningBoard, cost_limit, nodes_expanded, max_fringe_size, max_search_depth)
            return lst
           
    return False        
